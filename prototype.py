import os
import os.path
import sys
import time


def main():

  filters = [
    lambda x: not x.startswith('.'),
  ]

  action = sys.argv[1] if len(sys.argv[1:]) else None
  cwd = os.getcwd()
  cache = {}

  try:

    while True:
      should_reload = False

      for dir, _, files in os.walk(cwd):

        if os.path.basename(dir).startswith('.'):
          continue

        for f in filters:
          files = filter(f, files)

        files = list(files)

        if dir in cache:
          if len(cache[dir]) != len(files):
            should_reload = True

        else:
          cache[dir] = {}

        for file_name in files:

          file_path = os.path.join(dir, file_name)
          modified = os.path.getmtime(file_path)

          if file_name in cache[dir]:
            if cache[dir][file_name] != modified:
              cache[dir][file_name] = modified
              should_reload = True

          else:
            cache[dir][file_name] = modified
            should_reload = True

        deletables = []
        for file_name in cache[dir]:
          file_path = os.path.join(dir, file_name)
          if not os.path.exists(file_path):
            deletables.append(file_name)

        for file_name in deletables:
          del cache[dir][file_name]

      if should_reload:
        if action:
          os.system('cls' if os.name == 'nt' else 'clear')
          os.system(action)

      time.sleep(0.4)

  except KeyboardInterrupt:
    pass


if __name__ == '__main__':
  main()
