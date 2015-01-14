import fileinput


def __main__():
  files = []
  lines = dict()
  name = None

  for line in fileinput.input():
    line = line.strip()
    if line.startswith("#"):
      continue
    curr_name = fileinput.filename()
    if name == curr_name:
      pass
    else:
      name = curr_name
      files.append(name)
    line_split = line.split("==", 1)
    if len(line_split) > 1:
      pkg, version = line_split
    else:
      pkg, version = line_split[0], None
    lines.setdefault(name, {}).setdefault(
      pkg.lower(), dict(
        pkg=pkg,
        version=version,
      ))

  pin_file = files.pop(0)
  ask = pin_file != "<stdin>"
  pins = lines[pin_file]

  for name in files:
    changes = []
    contents = ""
    for pkg in sorted(lines[name]):
      pinned = pins.get(pkg)

      # Remove unused packages
      if not pinned:
        continue

      current = lines[name].get(pkg)

      # TODO: Compare versions
      if pinned["version"] != current["version"]:
        changes.append((current, pinned))

      contents += "{pkg}=={version}\n".format(**pinned)

    print name

    for current, pinned in changes:
      print "  {:<20}{} -> {}".format(
        pinned["pkg"],
        current["version"],
        pinned["version"],
      )
    print

    proceed = (
      raw_input("Do you want to continue? [Y/n] ")
      if ask else "y"
    )

    if proceed == "y":
      with open(name, "wb") as f:
        f.write(contents)


if __name__ == "__main__":
  __main__()
