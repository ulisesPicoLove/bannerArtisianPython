import os
import glob
import shutil
import zipfile
import re
from jinja2 import Environment, FileSystemLoader


class BannerGenerator:
    def __init__(self, work_dir):
        self.template_dir = os.path.join(os.path.dirname(__file__), "templates")
        self.output_base_dir = os.path.join(work_dir, "output")
        self.stack_base_dir = os.path.join(work_dir, "stack")
        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def normalize_stack(self, directory):
        stack_dir = os.path.join(self.stack_base_dir, directory)
        for root, dirs, files in os.walk(stack_dir):
            # Normaliza los nombres de las carpetas
            for dir_name in dirs:
                new_dir_name = re.sub(r"[×X]", "x", dir_name)  # Cambia × o X por x
                old_dir_path = os.path.join(root, dir_name)
                new_dir_path = os.path.join(root, new_dir_name)

                if old_dir_path != new_dir_path:
                    os.rename(old_dir_path, new_dir_path)
                    print(f"Renombrado directorio: {old_dir_path} -> {new_dir_path}")

            # Normaliza los nombres de los archivos
            for file_name in files:
                # Cambia × o X por x, reemplaza "_" por "-" y elimina ceros iniciales en números
                new_file_name = re.sub(r"[×X]", "x", file_name)
                new_file_name = new_file_name.replace("_", "-")

                old_file_path = os.path.join(root, file_name)
                new_file_path = os.path.join(root, new_file_name)

                if old_file_path != new_file_path:
                    os.rename(old_file_path, new_file_path)
                    print(f"Renombrado archivo: {old_file_path} -> {new_file_path}")

    def generate_banners(self, directory):
        banner_sizes = [
            "120x600",
            "160x600",
            "200x200",
            "240x400",
            "250x250",
            "250x360",
            "280x120",
            "300x50",
            "300x250",
            "300x600",
            "300x1050",
            "320x50",
            "320x100",
            "320x480",
            "336x280",
            "468x60",
            "580x400",
            "600x740",
            "600x800",
            "728x90",
            "920x250",
            "930x180",
            "930x1080",
            "970x90",
            "970x250",
            "980x120",
        ]

        output_dir = os.path.join(self.output_base_dir, directory)
        os.makedirs(output_dir, exist_ok=True)

        for size in banner_sizes:
            source_dir = os.path.join(self.stack_base_dir, directory, size)
            target_dir = os.path.join(output_dir, size)
            if os.path.isdir(source_dir):
                os.makedirs(target_dir, exist_ok=True)
                self.process_files(source_dir, target_dir, size)

    def process_files(self, source_dir, target_dir, size):
        image_files = glob.glob(
            os.path.join(source_dir, "*.{jpeg,jpg}"), recursive=True
        )
        total_size = 0

        for index, file_path in enumerate(image_files):
            file_size = os.path.getsize(file_path)
            total_size += file_size
            new_file_name = f"{size.upper()}_0{index + 1}.jpg"
            shutil.copy(file_path, os.path.join(target_dir, new_file_name))

        if total_size >= 100000:
            self.optimize_images(target_dir, image_files, size)

        self.copy_images(source_dir, target_dir)
        self.create_html(target_dir, size)
        self.create_zip(target_dir)

    def copy_images(self, source_dir, target_dir):
        for file_path in glob.glob(os.path.join(source_dir, "*")):
            if os.path.isfile(file_path):
                shutil.copy(file_path, target_dir)

    def optimize_images(self, target_dir, image_files, size):
        total_size = 0

        for index, file_path in enumerate(image_files):
            optimized_file_path = os.path.join(
                target_dir, f"{size.upper()}_0{index + 1}.jpg"
            )
            os.system(f"jpegoptim --size=33Kb {optimized_file_path}")
            file_size = os.path.getsize(optimized_file_path)
            total_size += file_size
            print(f"{optimized_file_path}: {file_size}")

        print(f"Total optimized size: {total_size}")

    def create_html(self, target_dir, size):
        width, height = size.split("x")
        template = self.env.get_template("index.html")
        html_content = template.render(WIDTH=width, HEIGHT=height)
        with open(os.path.join(target_dir, "index.html"), "w") as html_file:
            html_file.write(html_content)

    def create_zip(self, target_dir):
        zip_file_path = f"{target_dir}.zip"
        with zipfile.ZipFile(zip_file_path, "w") as zip_file:
            for root, _, files in os.walk(target_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.relpath(file_path, target_dir))
