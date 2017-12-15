#!/usr/bin/env python3

import sys
import re

class NodeInfo:
	def __init__(self, name, weight, children):
		self.name = name
		self.weight = weight
		self.children = children
		self.total_weight = None

	def __repr__(self):
		return 'NodeInfo(name=%s, weight=%s, total_weight=%s)' % (
				repr(self.name),
				repr(self.weight),
				repr(self.total_weight)
		)

	def name_to_references(self, nodeinfo):
		self.children = [nodeinfo[name] for name in self.children]
		for child in self.children:
			child.name_to_references(nodeinfo)

	def calculate_total(self):
		total = self.weight

		for child in self.children:
			total += child.calculate_total()

		self.total_weight = total
		return total

	def fix_unbalanced(self, target_weight=None):
		if len(self.children) >= 2:
			sorted_child = sorted(self.children, key=lambda x: x.total_weight)
			first = sorted_child[0]
			last = sorted_child[-1]
			other = sorted_child[1]

			if first.total_weight != last.total_weight:
				if first.total_weight == other.total_weight:
					return last.fix_unbalanced(other.total_weight)
				else:
					return first.fix_unbalanced(other.total_weight)

		self.weight -= self.total_weight - target_weight
		self.total_weight = target_weight

		return self

	def print_tree(self, depth=0):
		if depth > 0:
			print('  ' * (depth - 1) + '└ ', end='')
		print(repr(self))

		for child in self.children:
			child.print_tree(depth + 1)

parents = dict()
nodeinfo = dict()

for info in sys.stdin:
	match = re.match(r'(\w+) \((\d+)\)(?: -> (.*))?', info)
	if not match:
		continue

	name = match.group(1)
	weight = int(match.group(2))

	children = match.group(3)
	if children:
		children = children.strip().split(', ')
		for child in children:
			parents[child] = name
	else:
		children = []

	nodeinfo[name] = NodeInfo(name, int(weight), children)

topnode = next(iter(parents.values()))
while topnode in parents:
	topnode = parents[topnode]
topnode = nodeinfo[topnode]

print('Top node: ' + repr(unbalanced))

topnode.name_to_references(nodeinfo)
topnode.calculate_total()

unbalanced = topnode.fix_unbalanced()
print('Unbalanced: ' + repr(unbalanced))

topnode.print_tree()
