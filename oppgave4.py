import matplotlib.pyplot as plt
from file_read import File
from pathlib import Path


def data_and_title_from_line(line):
    title = line[0]
    data = [(int(value) if value.isnumeric() else 0) for value in line[1:]]
    return title, data


# Leser 'Skilsmisser og ekteskap.csv' med ";" som delimiter.
filnavn = 'Skilsmisser og ekteskap.csv'

skilsmisser_og_ekteskap_data = File(Path(__file__).parent /
                                    filnavn, delimiter=";").content


# Den første linjen i filen er tittelen
tittel = skilsmisser_og_ekteskap_data[0]

# Årstall fra data og bruker det som x_verdier
_, x_initial = data_and_title_from_line(
    skilsmisser_og_ekteskap_data[2])

# Dataen starter på linje 4
data_start_index = 3
bar_width = 4

# Vi går gjennom alle linjer fra fjerde linje og får tittel og data og plotter det med x_width margin mellom dem
for i in range(data_start_index, len(skilsmisser_og_ekteskap_data)):
    subtitle, data = data_and_title_from_line(
        skilsmisser_og_ekteskap_data[i])
    x_list = [(x+bar_width*(i-data_start_index))
              for x in x_initial]
    plt.bar(x_list, data, label=subtitle, width=bar_width)


xlabel = "År"
ylabel = "Inngåtte ekteskap og skilsmisser"

plt.legend()
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(tittel)

if __name__ == '__main__':
    plt.show()
