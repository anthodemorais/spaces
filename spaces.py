from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description="Searches and replaces in filenames.")
parser.add_argument("path", help="the path to replace in")
parser.add_argument("--recurse", help="replaces spaces with underscores in the subdirectories filenames too", required=False, action="store_true")
parser.add_argument("--search", help="the character to look for, default is ' '", required=False, default=" ")
parser.add_argument("--replace", help="the character to to replace with; default is '_'", required=False, default="_")

args = parser.parse_args()
pattern = "*"
if args.recurse is not None:
    pattern = "**/*"

for child in list(Path(args.path).glob(pattern)):
    name = child.name.replace(args.search, args.replace)
    child.rename(child.parent / name)