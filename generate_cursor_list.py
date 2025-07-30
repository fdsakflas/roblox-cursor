import os

def generate_cursor_list_readable(cursors_root="Cursors", output_file="cursor-list.txt"):
    cursor_names = set()
    preview_map = {}

    for root, dirs, files in os.walk(cursors_root):
        png_files = [f for f in files if f.lower().endswith(".png")]
        if png_files:
            folder_name = os.path.basename(root)  # Tylko ostatni folder
            if folder_name not in cursor_names:
                cursor_names.add(folder_name)
                preview_map[folder_name] = png_files[0]

    with open(output_file, "w", encoding="utf-8") as f:
        for name in sorted(cursor_names):
            f.write(name + "\n")

    print("Znalezione kursory:")
    for name in sorted(cursor_names):
        print(f"- {name} (preview: {preview_map[name]})")

    print(f"\nLista zapisana w pliku '{output_file}'")

if __name__ == "__main__":
    generate_cursor_list_readable()
