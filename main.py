from argparse import ArgumentParser
from generator import BannerGenerator

if __name__ == "__main__":
    parser = ArgumentParser(description='Generate banner images.')
    parser.add_argument('directory', type=str, help='Directory name to process')
    parser.add_argument('--workdir', type=str, default='./', help='Working directory')
    args = parser.parse_args()

    banner_generator = BannerGenerator(args.workdir)
    banner_generator.generate_banners(args.directory)
