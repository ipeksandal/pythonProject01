class FileError(Exception):
    pass


class EmptyFileError(FileError):
    pass


class DataError(FileError):
    pass


def read_scores(filename):
    scores = {}

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if not lines:
                raise EmptyFileError("Dosya boş.")

            for line in lines:
                parts = line.strip().split()
                if len(parts) != 3:
                    raise DataError(f"Veri hatası: '{line.strip()}'")

                name, surname, score = parts
                try:
                    score = float(score)
                except ValueError:
                    raise DataError(f"Geçersiz puan: '{score}'")

                full_name = f"{name} {surname}"
                if full_name in scores:
                    scores[full_name] += score
                else:
                    scores[full_name] = score

    except FileNotFoundError:
        raise FileError("Dosya bulunamadı.")

    return scores


def print_scores(scores):
    for student in sorted(scores.keys()):
        print(f"{student}\t{scores[student]:.1f}")


def main():
    filename = input("Prof. Jekyll'in dosya adını girin: ")

    try:
        scores = read_scores(filename)
        if scores:
            print_scores(scores)
        else:
            print("Dosya boş veya geçersiz veri içeriyor.")
    except FileError as e:
        print(f"Hata: {e}")


if __name__ == "__main__":
    main()
