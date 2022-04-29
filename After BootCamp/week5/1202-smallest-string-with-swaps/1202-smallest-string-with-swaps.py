class Solution:
	def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

		graph = defaultdict(list)
		for a,b in pairs:
			graph[a].append(b)
			graph[b].append(a)

		col = []
		self.seen = set()
		def grp_making(point):
			nonlocal local
			if point in self.seen:
				return

			local.append(point)
			self.seen.add(point)
			for p in graph[point]:
				grp_making(p)

		for k in graph.keys():
			if k not in self.seen:
				local = []
				grp_making(k)
				col.append(local)

		res = list(s)
		for grp in col:
			tmp = ""
			for ind in grp:
				tmp += s[ind]
			tmp = sorted(tmp)
			grp.sort()
			i = 0
			for ind in grp:
				res[ind] = tmp[i]
				i+=1

		return ''.join(res)