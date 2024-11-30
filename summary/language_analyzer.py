import os

extension_to_language = {
  '.java': 'Java',
  '.cpp': 'C++',
  '.py': 'Python',
  '.js': 'JavaScript',
  '.ts': 'TypeScript',
  '.ipynb': 'Jupyter Notebook',
  '.c': 'C',
  '.rb': 'Ruby',
  '.go': 'Go',
  '.html': 'HTML',
  '.css': 'CSS',
  '.php': 'PHP',
  '.swift': 'Swift',
  '.kt': 'Kotlin',
  '.rs': 'Rust',
  '.sh': 'Shell',
  '.pl': 'Perl',
  '.r': 'R',
  '.m': 'MATLAB',
  '.scala': 'Scala',
  '.lua': 'Lua',
  '.hs': 'Haskell',
  '.erl': 'Erlang',
  '.ex': 'Elixir',
  '.clj': 'Clojure',
  '.dart': 'Dart',
  '.jl': 'Julia',
  '.groovy': 'Groovy',
  '.f90': 'Fortran',
  '.v': 'Verilog',
  '.vhdl': 'VHDL',
  '.asm': 'Assembly',
  '.bat': 'Batch',
  '.ps1': 'PowerShell',
  '.sql': 'SQL',
  '.xml': 'XML',
  '.json': 'JSON',
  '.yaml': 'YAML',
  '.ini': 'INI',
  '.toml': 'TOML',
  '.md': 'Markdown',
  '.rst': 'reStructuredText',
  '.tex': 'LaTeX',
  '.adoc': 'AsciiDoc',
}


class LanguageAnalyzer:

  @staticmethod
  def detect_language(filename) -> str:
    _, extension = os.path.splitext(filename)
    return extension_to_language.get(extension, 'Undefined')
