amount = int(input())

compounds = ['(○ ○)', ' /V\\ ', '/(_)\\', '^^ ^^']

for c in compounds:
    print("\t".join([c] * amount))
