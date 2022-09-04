using Toybox.System as Sys;
using Toybox.Lang;

// these guys are in global namespace due to handiness
const print = Sys.println;
const format = Lang.format;

module MyStringUtils {
  const NEWLINE = "\n";

  function charAt(string, index) {
    return string.substring(index, index + 1);
  }

  function isWhitespace(string) {
    return string.equals(" ");
  }

  function examine(string) {
    var offset = 30;
    var length = string.length();
    var head = string.substring(0, offset);
    var tail = string.substring(length - offset, length);
    print(format("length: $1$\nhead: $2$\ntail: $3$", [length, head, tail]));
  }
}
