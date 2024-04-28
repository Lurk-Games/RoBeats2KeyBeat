def replace_words_and_characters_in_file(input_file_path, output_file_path):
  replacements = {
      "note": "",
      "hold": "",
      "(": "{",
      ")": "}",
      " ": ";"
  }

  with open(input_file_path, "r") as infile, open(output_file_path, "w") as outfile:
      for line in infile:
          for src, target in replacements.items():
              line = line.replace(src, target)
          outfile.write(line)

# Example usage:
input_file = "input.txt"
output_file = "output.txt"
replace_words_and_characters_in_file(input_file, output_file)
print(f"Text successfully replaced in {output_file}")
