import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2lab, deltaE_cie76
from IPython.display import display
import ipywidgets as widgets

def upload_image():
    uploader = widgets.FileUpload(accept='.jpg,.png,.jpeg', multiple=False)
    display(uploader)

    while not uploader.value:
    pass

    uploaded_file = list(uploader.value.values())[0]
    file_name = uploaded_file['name']
    with open(file_name, "wb") as f:
        f.write(uploaded_file['content'])
    
    return file_name

def rgb_to_cmyk(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_rgb = image_rgb / 255.0
    cmy = 1 - image_rgb
    k = np.min(cmy, axis=2)
    k_expanded = k[..., np.newaxis]
    denominator = 1 - k_expanded
    denominator = np.where(denominator == 0, np.finfo(float).eps, denominator)
    cmy = (cmy - k_expanded) / denominator
    cmyk = np.concatenate([cmy, k_expanded], axis=-1)
    return cmyk

def color_difference(target, hasil):
    hasil_resized = cv2.resize(hasil, (target.shape[1], target.shape[0]))
    target_lab = rgb2lab(target)
    hasil_lab = rgb2lab(hasil_resized)
    delta_e = deltaE_cie76(target_lab, hasil_lab)
    avg_delta_e = np.mean(delta_e)
    return avg_delta_e

def display_images_and_channels(target, hasil, cmyk_target, cmyk_hasil):
    fig, axes = plt.subplots(2, 5, figsize=(20, 6))

    axes[0, 0].imshow(cv2.cvtColor(target, cv2.COLOR_BGR2RGB))
    axes[0, 0].set_title("Target")
    axes[0, 0].axis('off')

    axes[0, 1].imshow(cmyk_target[:, :, 0], cmap='Blues')  # Cyan
    axes[0, 1].set_title("Cyan (C)")
    axes[0, 1].axis('off')

    axes[0, 2].imshow(cmyk_target[:, :, 1], cmap='viridis')  # Magenta
    axes[0, 2].set_title("Magenta (M)")
    axes[0, 2].axis('off')

    axes[0, 3].imshow(cmyk_target[:, :, 2], cmap='YlOrBr')  # Yellow
    axes[0, 3].set_title("Yellow (Y)")
    axes[0, 3].axis('off')

    axes[0, 4].imshow(cmyk_target[:, :, 3], cmap='gray')  # Black
    axes[0, 4].set_title("Black (K)")
    axes[0, 4].axis('off')

    axes[1, 0].imshow(cv2.cvtColor(hasil, cv2.COLOR_BGR2RGB))
    axes[1, 0].set_title("Hasil")
    axes[1, 0].axis('off')

    axes[1, 1].imshow(cmyk_hasil[:, :, 0], cmap='Blues')  # Cyan
    axes[1, 1].set_title("Cyan (C)")
    axes[1, 1].axis('off')

    axes[1, 2].imshow(cmyk_hasil[:, :, 1], cmap='viridis')  # Magenta
    axes[1, 2].set_title("Magenta (M)")
    axes[1, 2].axis('off')

    axes[1, 3].imshow(cmyk_hasil[:, :, 2], cmap='YlOrBr')  # Yellow
    axes[1, 3].set_title("Yellow (Y)")
    axes[1, 3].axis('off')

    axes[1, 4].imshow(cmyk_hasil[:, :, 3], cmap='gray')  # Black
    axes[1, 4].set_title("Black (K)")
    axes[1, 4].axis('off')

    plt.tight_layout()
    plt.show()

def color_density(cmyk_image):
    cyan_density = np.mean(cmyk_image[:, :, 0]) * 100
    magenta_density = np.mean(cmyk_image[:, :, 1]) * 100
    yellow_density = np.mean(cmyk_image[:, :, 2]) * 100
    black_density = np.mean(cmyk_image[:, :, 3]) * 100

    densities = {
        "Cyan Density": cyan_density,
        "Magenta Density": magenta_density,
        "Yellow Density": yellow_density,
        "Black Density": black_density
    }

    for label, value in densities.items():
        print(f"{label}: {value:.2f}%")

    return list(densities.values())

def color_solidarity(cmyk_image):
    cyan_solidarity = np.std(cmyk_image[:, :, 0]) * 100
    magenta_solidarity = np.std(cmyk_image[:, :, 1]) * 100
    yellow_solidarity = np.std(cmyk_image[:, :, 2]) * 100
    black_solidarity = np.std(cmyk_image[:, :, 3]) * 100

    solidarities = {
        "Cyan Solidarity": cyan_solidarity,
        "Magenta Solidarity": magenta_solidarity,
        "Yellow Solidarity": yellow_solidarity,
        "Black Solidarity": black_solidarity
    }

    for label, value in solidarities.items():
        print(f"{label}: {value:.2f}%")

    return list(solidarities.values())

# Menghitung statistik
def compare_images(density_target, density_hasil, solidarity_target, solidarity_hasil):
    comparison = {
        "Cyan (C)": density_target[0] - density_hasil[0],
        "Magenta (M)": density_target[1] - density_hasil[1],
        "Yellow (Y)": density_target[2] - density_hasil[2],
        "Black (K)": density_target[3] - density_hasil[3],
    }
    return comparison

# Menampilkan statistik dalam bentuk grafik
def plot_comparison_stats(comparison):
    labels = list(comparison.keys())
    values = list(comparison.values())

    plt.figure(figsize=(10, 6))
    plt.bar(labels, values, color=['blue', 'red', 'green', 'black'])
    plt.xlabel('Parameter')
    plt.ylabel('Perbedaan')
    plt.title('Statistik Perbandingan antara Gambar')
    plt.xticks(rotation=45, ha='left')
    plt.tight_layout()
    plt.show()

# Grafik perbandingan perbedaan warna
def plot_color_difference(density_target, density_hasil):
    labels = ['Cyan', 'Magenta', 'Yellow', 'Black']
    x = np.arange(len(labels))

    fig, ax = plt.subplots()

    ax.plot(x, density_target, marker='o', label='Target', color='blue', linestyle='-', linewidth=2)
    ax.plot(x, density_hasil, marker='o', label='Hasil', color='red', linestyle='-', linewidth=2)

    ax.set_ylabel('Density (%)')
    ax.set_title('Perbandingan Warna CMYK')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    # Add labels only if they are finite values
    for i in range(len(x)):
        if np.isfinite(density_target[i]):
            ax.text(x[i], density_target[i] + 1, f'{density_target[i]:.2f}%', ha='center', color='blue')
        else:
            ax.text(x[i], 0, 'N/A', ha='center', color='blue')  # or skip with `continue`

        if np.isfinite(density_hasil[i]):
            ax.text(x[i], density_hasil[i] + 1, f'{density_hasil[i]:.2f}%', ha='center', color='red')
        else:
            ax.text(x[i], 0, 'N/A', ha='center', color='red')  # or skip with `continue`

    fig.tight_layout()
    plt.show()

# Analisis colorimetric
def analyze_printing_color():
    print("Upload Gambar Target:")
    target_file = upload_image()
    print("Upload Gambar Hasil:")
    hasil_file = upload_image()

    # Reading Image
    target = cv2.imread(target_file)
    hasil = cv2.imread(hasil_file)

    if target is None:
        raise ValueError(f"Gagal membaca gambar target: {target_file}")
    if hasil is None:
        raise ValueError(f"Gagal membaca gambar hasil: {hasil_file}")

    # Mengubah warna RGB ke warna CMYK
    cmyk_target = rgb_to_cmyk(target)
    cmyk_hasil = rgb_to_cmyk(hasil)

    # Menghitung perbedaan warna (Delta E) antara gambar.
    delta_e = color_difference(target, hasil)

    # Menghitung density warna dan kesolidan untuk kedua gambar
    density_target, density_hasil = color_density(cmyk_target), color_density(cmyk_hasil)
    solidarity_target, solidarity_hasil = color_solidarity(cmyk_target), color_solidarity(cmyk_hasil)

    # Menampilkan gambar dan channel CMYK
    display_images_and_channels(target, hasil, cmyk_target, cmyk_hasil)

    # Menampilkan grafik perbandingan perbedaan warna
    plot_color_difference(density_target, density_hasil)

    # Menampilkan statistik perbandingan antara kedua gambar
    comparison = compare_images(density_target, density_hasil, solidarity_target, solidarity_hasil)
    plot_comparison_stats(comparison)

# Proses..
analyze_printing_color()
