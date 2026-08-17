import numpy as np
import matplotlib.pyplot as plt

# Bins from 0 to 40 with uniform width of 2
bin_edges = np.arange(0, 42, 2)  # 0, 2, 4, ..., 40
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2.0  # 1, 3, 5, ..., 39

# Exact visual percentages from the datasheet histogram:
probs_percent = np.array(
    [
        10.3,
        23.7,
        14.1,
        14.1,
        10.7,
        7.6,
        5.6,
        5.3,
        3.9,
        1.3,
        1.6,
        1.1,
        0.9,
        0.3,
        0.6,
        0.3,
        0.3,
        0.3,
        0.3,
        0.0,
    ]
)

# Scale probabilities to sum to 100%
probs_percent = probs_percent / probs_percent.sum() * 100.0

# Calculate Lognormal fit parameters in pure NumPy
# Sample weighted by probs
np.random.seed(42)
probs_norm = probs_percent / 100.0
bin_indices = np.random.choice(len(probs_norm), size=500000, p=probs_norm)
samples = np.array(
    [np.random.uniform(bin_edges[i], bin_edges[i + 1]) for i in bin_indices]
)

log_samples = np.log(samples)
mu = np.mean(log_samples)
sigma = np.std(log_samples)


# Lognormal PDF (integrates to 1)
def lognormal_pdf(x, mu, sigma):
    return (1.0 / (x * sigma * np.sqrt(2 * np.pi))) * np.exp(
        -((np.log(x) - mu) ** 2) / (2 * sigma**2)
    )


# Convert PDF to "Percent per 2 uV/degC bin"
# Height in % = PDF(x) * bin_width (2) * 100
x = np.linspace(0.01, 40, 1000)
pdf_y_percent = lognormal_pdf(x, mu, sigma) * 2.0 * 100.0

# Plotting directly matching datasheet Y-axis (Percent of Amplifiers %)
fig, ax = plt.subplots(figsize=(9, 5.5), dpi=150)

# Bar chart with exact percentage heights
ax.bar(
    bin_centers,
    probs_percent,
    width=2.0,
    align="center",
    alpha=0.5,
    color="#a6bddb",
    edgecolor="black",
    linewidth=0.8,
    label="Production Distribution (Datasheet Bars)",
)

# Overlay scaled Lognormal curve
ax.plot(
    x,
    pdf_y_percent,
    color="#d62728",
    lw=2.5,
    label=f"Lognormal Fit ($\mu$={mu:.2f}, $\sigma$={sigma:.2f})",
)

ax.set_title(
    "OFFSETS VOLTAGE DRIFT PRODUCTION DISTRIBUTION",
    fontsize=12,
    fontweight="bold",
    pad=12,
)
ax.set_xlabel("Offset Voltage Drift ($\mu$V/Â°C)", fontsize=11)
ax.set_ylabel("Percent of Amplifiers (%)", fontsize=11)
ax.set_xlim(0, 40)
ax.set_ylim(0, 25)
ax.set_yticks(np.arange(0, 26, 5))
ax.grid(True, linestyle="--", alpha=0.4, axis="y")
ax.legend(fontsize=10, loc="upper right")

plt.tight_layout()
plt.savefig("datasheet_percent_scale_fit.png")
plt.show()
