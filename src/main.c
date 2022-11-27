#include "sjpslib/std.h"


i32 main(i32 argc, string argv[]) begin

  when argc < 2
  then return$(0, println("Missing command!"));

  string command = argv[1];
  u64 cache[512];
  bool did_update;
  Process p;
  FileInfo fi;
  FileInfoList fil;

  strfmt(cwd, 2048, "%s", getcwd(cwd, 2048));

  loop begin

    did_update = false;

    FileInfoList_init(ref fil, 512);
    list_files(cwd, ref fil);

    countup (index, 0, fil.len) begin

      fi = FileInfoList_get(ref fil, index);

      when cache[index] != fi.written
      then begin
        cache[index] = fi.written;
        did_update = true;
      end

    end

    when did_update
    then begin
      proc_kill(ref p);
      p = proc_spawn(command);
    end

    FileInfoList_free(ref fil);
    sleep(100);

  end

  return 0;

end
