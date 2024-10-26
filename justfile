default:
	just --list

fmt:
	trunk fmt

check:
	trunk check

fix:
	trunk check -y

pr:
	gh pr create

all:
	trunk fmt -a
	trunk check -a

push: all pr
