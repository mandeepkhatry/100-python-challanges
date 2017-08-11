

unsorted = input()

uslist = [x for x in unsorted.split(',')]

uslist.sort()

print(",".join(uslist))


