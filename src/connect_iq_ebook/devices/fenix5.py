from .base import BaseDevice


class Fenix5(BaseDevice):

    max_chunk_size = 8000  # arbitrary
    family_qualifier = 'round-240x240'

    def char_to_width(self, char):
        return XTINY_WIDTHS.get(char, XTINY_FALLBACK)

    @property
    def lines_geometry(self):
        return XTINY_FILL_LINES


XTINY_FILL_LINES = [
    [61, 15, 117, 22],
    [28, 42, 183, 22],
    [11, 69, 218, 22],
    [2, 96, 236, 22],
    [2, 123, 235, 22],
    [11, 150, 217, 22],
    [29, 177, 181, 22],
    [63, 204, 113, 22]
]

XTINY_FALLBACK = 12
XTINY_WIDTHS = {
    r'!': 5,
    r'"': 7,
    r'#': 12,
    r'$': 11,
    r'%': 14,
    r'&': 12,
    r'\'': 4,
    r'(': 7,
    r')': 7,
    r'*': 9,
    r'+': 11,
    r',': 4,
    r'-': 5,
    r'.': 6,
    r'/': 8,
    r'0': 11,
    r'1': 11,
    r'2': 11,
    r'3': 11,
    r'4': 11,
    r'5': 11,
    r'6': 11,
    r'7': 11,
    r'8': 11,
    r'9': 11,
    r':': 5,
    r';': 4,
    r' ': 5,
    r'<': 10,
    r'=': 10,
    r'>': 10,
    r'?': 9,
    r'@': 17,
    r'A': 12,
    r'B': 12,
    r'C': 12,
    r'D': 12,
    r'E': 11,
    r'F': 10,
    r'G': 13,
    r'H': 13,
    r'I': 5,
    r'J': 10,
    r'K': 12,
    r'L': 10,
    r'M': 16,
    r'N': 13,
    r'O': 13,
    r'P': 12,
    r'Q': 13,
    r'R': 11,
    r'S': 11,
    r'T': 11,
    r'U': 12,
    r'V': 12,
    r'W': 16,
    r'X': 12,
    r'Y': 11,
    r'Z': 11,
    r'[': 5,
    r'\\': 8,
    r']': 5,
    r'^': 8,
    r'_': 9,
    r'`': 7,
    r'a': 10,
    r'b': 11,
    r'c': 10,
    r'd': 11,
    r'e': 10,
    r'f': 7,
    r'g': 11,
    r'h': 10,
    r'i': 5,
    r'j': 5,
    r'k': 10,
    r'l': 5,
    r'm': 16,
    r'n': 10,
    r'o': 11,
    r' ': 5,
    r'p': 11,
    r'q': 11,
    r'r': 7,
    r's': 10,
    r't': 6,
    r'u': 10,
    r'v': 9,
    r'w': 14,
    r'x': 10,
    r'y': 9,
    r'z': 10,
    r'{': 7,
    r'|': 5,
    r'}': 7,
    r'~': 13,
    r' ': 5,
    r'¡': 5,
    r'¢': 10,
    r'£': 11,
    r'¤': 15,
    r'¥': 11,
    r'¦': 5,
    r'§': 12,
    r'¨': 9,
    r'©': 17,
    r'ª': 9,
    r'«': 9,
    r'¬': 11,
    r'­': 0,
    r'®': 17,
    r'¯': 9,
    r'°': 8,
    r'±': 10,
    r'²': 7,
    r'³': 7,
    r'´': 7,
    r'µ': 11,
    r'¶': 9,
    r'·': 5,
    r'¸': 5,
    r'¹': 7,
    r'º': 9,
    r'»': 9,
    r'¼': 14,
    r'½': 15,
    r'¾': 15,
    r'¿': 9,
    r'À': 12,
    r'Á': 12,
    r'Â': 12,
    r'Ã': 12,
    r'Ä': 12,
    r'Å': 12,
    r' ': 5,
    r'Æ': 18,
    r'Ç': 12,
    r'È': 11,
    r'É': 11,
    r'Ê': 11,
    r'Ë': 11,
    r'Ì': 5,
    r'Í': 5,
    r'Î': 5,
    r'Ï': 5,
    r'Ð': 13,
    r'Ñ': 13,
    r'Ò': 13,
    r'Ó': 13,
    r'Ô': 13,
    r'Õ': 13,
    r'Ö': 13,
    r'×': 10,
    r'Ø': 13,
    r'Ù': 12,
    r'Ú': 12,
    r'Û': 12,
    r'Ü': 12,
    r'Ý': 11,
    r'Þ': 11,
    r' ': 5,
    r'ß': 11,
    r'à': 10,
    r'á': 10,
    r'â': 10,
    r'ã': 10,
    r'ä': 10,
    r'å': 10,
    r'æ': 16,
    r'ç': 10,
    r'è': 10,
    r'é': 10,
    r'ê': 10,
    r'ë': 10,
    r'ì': 5,
    r'í': 5,
    r'î': 5,
    r'ï': 5,
    r'ð': 11,
    r'ñ': 10,
    r'ò': 11,
    r'ó': 11,
    r'ô': 11,
    r'õ': 11,
    r'ö': 11,
    r'÷': 11,
    r' ': 5,
    r'ø': 11,
    r'ù': 10,
    r'ú': 10,
    r'û': 10,
    r'ü': 10,
    r'ý': 9,
    r'þ': 11,
    r'ÿ': 9,
    r'Ă': 12,
    r'ă': 10,
    r'Ą': 12,
    r'ą': 10,
    r'Ć': 12,
    r'ć': 10,
    r'Č': 12,
    r'č': 10,
    r'Ď': 12,
    r'ď': 12,
    r'Đ': 13,
    r'đ': 11,
    r'Ē': 11,
    r'ē': 10,
    r'Ę': 11,
    r'ę': 10,
    r' ': 5,
    r'Ě': 11,
    r'ě': 10,
    r'Ĺ': 10,
    r'ĺ': 5,
    r'Ľ': 10,
    r'ľ': 7,
    r'Ł': 10,
    r'ł': 5,
    r'Ń': 13,
    r'ń': 10,
    r'Ň': 13,
    r'ň': 10,
    r'Ő': 13,
    r'ő': 11,
    r'Œ': 18,
    r'œ': 17,
    r'Ŕ': 11,
    r'ŕ': 7,
    r'Ř': 11,
    r'ř': 7,
    r'Ś': 11,
    r'ś': 10,
    r'Ş': 11,
    r'ş': 10,
    r'Š': 11,
    r'š': 10,
    r' ': 5,
    r'Ţ': 11,
    r'ţ': 6,
    r'Ť': 11,
    r'ť': 7,
    r'Ů': 12,
    r'ů': 10,
    r'Ű': 12,
    r'ű': 10,
    r'Ÿ': 11,
    r'Ź': 11,
    r'ź': 10,
    r'Ż': 11,
    r'ż': 10,
    r'Ž': 11,
    r'ž': 10,
    r'ƒ': 7,
    r'ˆ': 9,
    r'ˇ': 9,
    r'˘': 9,
    r'˙': 5,
    r'˛': 5,
    r'˜': 9,
    r'˝': 7,
    r'΄': 6,
    r' ': 5,
    r'΅': 10,
    r'Ά': 12,
    r'Έ': 12,
    r'Ή': 14,
    r'Ί': 6,
    r'Ό': 13,
    r'Ύ': 12,
    r'Ώ': 13,
    r'ΐ': 6,
    r'Α': 12,
    r'Β': 12,
    r'Γ': 11,
    r'Δ': 13,
    r'Ε': 11,
    r'Ζ': 11,
    r'Η': 13,
    r'Θ': 13,
    r'Ι': 5,
    r'Κ': 12,
    r'Λ': 12,
    r'Μ': 16,
    r'Ν': 13,
    r'Ξ': 11,
    r'Ο': 13,
    r'Π': 13,
    r' ': 5,
    r'Ρ': 12,
    r'Σ': 11,
    r'Τ': 11,
    r'Τ': 11,
    r'Υ': 11,
    r'Φ': 13,
    r'Χ': 12,
    r'Ψ': 13,
    r'Ω': 13,
    r'Ϊ': 5,
    r'Ϋ': 11,
    r'ά': 11,
    r'έ': 10,
    r'ή': 11,
    r'ί': 6,
    r'ΰ': 10,
    r'α': 11,
    r'β': 11,
    r'γ': 10,
    r'δ': 11,
    r'ε': 10,
    r'ζ': 10,
    r'η': 11,
    r'θ': 11,
    r'ι': 6,
    r'κ': 11,
    r'λ': 11,
    r'μ': 11,
    r'ν': 9,
    r'ξ': 9,
    r'ο': 11,
    r' ': 5,
    r'π': 11,
    r'ρ': 11,
    r'ς': 10,
    r'σ': 11,
    r'τ': 10,
    r'υ': 10,
    r'φ': 13,
    r'χ': 10,
    r'ψ': 13,
    r'ω': 15,
    r'ϊ': 6,
    r'ϊ': 6,
    r'ϋ': 10,
    r'ό': 11,
    r'ύ': 10,
    r'ώ': 15,
    r'Ё': 11,
    r'Ђ': 14,
    r'Ѓ': 11,
    r'Є': 13,
    r'Ѕ': 11,
    r'І': 5,
    r'Ї': 5,
    r'Ј': 10,
    r'Љ': 20,
    r'Њ': 20,
    r' ': 5,
    r'Ћ': 15,
    r'Ќ': 12,
    r'Ў': 12,
    r'Џ': 13,
    r'А': 12,
    r'Б': 12,
    r'В': 12,
    r'Г': 11,
    r'Д': 14,
    r'Е': 11,
    r'Ж': 17,
    r'З': 11,
    r'И': 13,
    r'Й': 13,
    r'К': 12,
    r'Л': 13,
    r'М': 16,
    r'Н': 13,
    r'О': 13,
    r'П': 13,
    r'Р': 12,
    r'С': 12,
    r'Т': 11,
    r'У': 12,
    r' ': 5,
    r'Ф': 15,
    r'Х': 12,
    r'Ц': 14,
    r'Ч': 13,
    r'Ш': 18,
    r'Щ': 18,
    r'Ъ': 14,
    r'Ы': 16,
    r'Ь': 12,
    r'Э': 13,
    r'Ю': 17,
    r'Я': 12,
    r'а': 10,
    r'б': 10,
    r'в': 11,
    r'г': 8,
    r'д': 12,
    r'е': 10,
    r'ж': 14,
    r'з': 10,
    r'и': 11,
    r'й': 11,
    r' ': 5,
    r'к': 10,
    r'л': 11,
    r'м': 14,
    r'н': 11,
    r'о': 11,
    r'п': 11,
    r'р': 11,
    r'с': 10,
    r'т': 9,
    r'у': 9,
    r'ф': 14,
    r'х': 10,
    r'ц': 11,
    r'ч': 10,
    r'ш': 15,
    r'щ': 16,
    r'ъ': 12,
    r'ы': 15,
    r'ь': 10,
    r'э': 10,
    r'ю': 15,
    r'я': 10,
    r' ': 5,
    r'ё': 10,
    r'ђ': 10,
    r'ѓ': 8,
    r'є': 10,
    r'ѕ': 10,
    r'і': 5,
    r'ї': 5,
    r'ј': 5,
    r'љ': 16,
    r'њ': 16,
    r'ћ': 11,
    r'ќ': 10,
    r'ў': 9,
    r'џ': 11,
    r'Ґ': 10,
    r'ґ': 9,
    r'–': 12,
    r'—': 15,
    r'―': 15,
    r'‘': 4,
    r'’': 4,
    r'‚': 4,
    r' ': 5,
    r'“': 7,
    r'”': 7,
    r'„': 7,
    r'†': 10,
    r'‡': 11,
    r'•': 7,
    r'…': 13,
    r'‰': 18,
    r'‹': 6,
    r'›': 6,
    r'€': 11,
    r'№': 19,
    r'™': 12,
    r'⏶': 17,
    r'⏷': 17,
    r'': 8,
    r'￼': 22,
}
