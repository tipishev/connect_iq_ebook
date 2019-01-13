module CharWidthsPrinter {
      // warning, contains Unicode voodoo codepoints
      const FENIX_5_AVAILABLE_CHARS = [
      "!\"#$%&'()*+,-./0123456789:; <=>?@ABCDEFGHIJKLMNOPQRSTUV",
      "WXYZ[\\]^_`abcdefghijklmno pqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­",
      "®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅ ÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞ ",
      "ßàáâãäåæçèéêëìíîïðñòóôõö÷ øùúûüýþÿĂăĄąĆćČčĎďĐđĒēĘę ",
      "ĚěĹĺĽľŁłŃńŇňŐőŒœŔŕŘřŚśŞşŠš ŢţŤťŮůŰűŸŹźŻżŽžƒˆˇ˘˙˛˜˝΄ ",
      "΅ΆΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠ ",
      "ΡΣΤΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξο πρςστυφχψωϊϊϋόύώЁЂЃЄЅІЇЈЉЊ ",
      "ЋЌЎЏАБВГДЕЖЗИЙКЛМНОПРСТУ ФХЦЧШЩЪЫЬЭЮЯабвгдежзий ",
      "клмнопрстуфхцчшщъыьэюя ёђѓєѕіїјљњћќўџҐґ–—―‘’‚ “”„†‡•…‰",
      "‹›€№™⏶⏷",
      "￼",
      /* "�" */
      ];

      function printCharsWidthsAsPythonDict(dc) {
        var line = "";
        for (var i = 0; i < FENIX_5_AVAILABLE_CHARS.size(); i++) {
          line += FENIX_5_AVAILABLE_CHARS[i];
        }

        // TODO properly escape backslash and single quote
        print("FENIX_5_FONT_XTINY_WIDTHS = {");
        for (var i = 0; i < line.length(); i++) {
          var char = charAt(line, i);
          print("    r'" + char + "'" + ": " +\
                dc.getTextWidthInPixels(char, FONT) + ",");
        }
        print("}");
      }
}

module CharWidthsPrinter {
      // warning, contains Unicode voodoo codepoints
      var FENIX_5S_AVAILABLE_CHARS = [
      "!\"#$%&'()*+,-./0123456789:; <=>?@ABCDEFGHIJKLMNOPQRSTUV",
      "WXYZ[\\]^_`abcdefghijklmno pqrstuvwxyz{|}~ ¡¢£¤¥¦§¨©ª«¬­",
      "®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅ ÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞ ",
      "ßàáâãäåæçèéêëìíîïðñòóôõö÷ øùúûüýþÿĂăĄąĆćČčĎďĐđĒēĘę ",
      "ĚěĹĺĽľŁłŃńŇňŐőŒœŔŕŘřŚśŞşŠš ŢţŤťŮůŰűŸŹźŻżŽžƒˆˇ˘˙˛˜˝΄ ",
      "΅ΆΈΉΊΌΎΏΐΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠ ",
      "ΡΣΤΤΥΦΧΨΩΪΫάέήίΰαβγδεζηθικλμνξο πρςστυφχψωϊϊϋόύώЁЂЃЄЅІЇЈЉЊ ",
      "ЋЌЎЏАБВГДЕЖЗИЙКЛМНОПРСТУ ФХЦЧШЩЪЫЬЭЮЯабвгдежзий ",
      "клмнопрстуфхцчшщъыьэюя ёђѓєѕіїјљњћќўџҐґ–—―‘’‚ “”„†‡•…‰",
      "‹›€№™⏶⏷",
      "￼",
      /* "�" */
      ];

      function printCharsWidthsAsPythonDict(dc) {
        var line = "";
        for (var i = 0; i < FENIX_5S_AVAILABLE_CHARS.size(); i++) {
          line += FENIX_5S_AVAILABLE_CHARS[i];
        }

        // TODO properly escape backslash and single quote
        print("FENIX_5S_FONT_XTINY_WIDTHS = {");
        for (var i = 0; i < line.length(); i++) {
          var char = charAt(line, i);
          print("    r'" + char + "'" + ": " +\
                dc.getTextWidthInPixels(char, Gfx.FONT_SYSTEM_XTINY) + ",");
        }
        print("}");
      }
}
