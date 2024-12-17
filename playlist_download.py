from download_yt import download_playlist
import argparse

def main(): 
    parser = argparse.ArgumentParser(description = 'Baixa todos os vídeos de uma playlist em formato de áudio mp3')
    parser.add_argument('link', action='store', help='Link da playlist')
    parser.add_argument('--dir', '-d', action='store', help='Diretório raiz onde será criado o diretório com os áudios da playlist')
    args = parser.parse_args()
    download_playlist(args.link, args.dir)

if __name__ == "__main__":
    main()