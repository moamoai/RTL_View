
sm:
	dot -T svg sm.dot -o tmp_sm.svg
	# cat tmp_sm.svg | awk '{sub("<!--.*.-->", "");print $0;}' > sm.svg
	# sed '/<!--/,/-->/d' tmp_sm.svg > sm.svg
	sed '/<!--.*-->/d' tmp_sm.svg > sm.svg
	sed -n '/<svg/,/<\svg>/p' sm.svg | pbcopy
