import matplotlib.pyplot as plt

# Sample data for the chart
categories = [
    "Office and administrative support", 
    "Transportation and material moving", 
    "Sales and related", 
    "Food preparation and serving related", 
    "General management", 
    "Business and financial operations", 
    "Healthcare practitioners and technical", 
    "Production services", 
    "Education instruction and library", 
    "Healthcare support", 
    "Construction and extraction", 
    "Installation, maintenance, and repair", 
    "Computer and mathematical", 
    "Building grounds cleaning and maintenance", 
    "Protective service", 
    "Personal care and service", 
    "Architecture and engineering", 
    "Community and social service", 
    "Arts, design, sports, entertainment, and media", 
    "Life, physical, and social science", 
    "Legal services", 
    "Farming, fishing, and forestry"
]

claude_representation = [
    7.9, 0.3, 2.3, 0.5, 4.5, 5.9, 2.6, 2.9, 9.3, 0.3, 0.4, 0.7, 
    37.2, 0.1, 0.4, 0.5, 
    4.5, 2.1, 10.3, 6.4, 0.9, 
    0.1
]

us_workers_representation = [
    12.2, 9.1, 8.8, 8.7, 6.9, 6.6, 6.1, 5.8, 5.8, 4.7, 4.1, 3.9, 
    3.4, 2.9, 2.3, 2.0, 
    1.7, 1.6, 1.4, 0.9, 0.8, 
    0.3
]

# Colors for Claude and U.S. workers
claude_color = "#da7757"
us_workers_color = "#4d4c48"

# Set figure size to 12x12
plt.figure(figsize=(10, 10))

for i, category in enumerate(categories):
    line_color = claude_color if us_workers_representation[i] < claude_representation[i] else us_workers_color
    plt.plot([claude_representation[i], us_workers_representation[i]], [i, i], color=line_color, lw=3.5, zorder=1)
    plt.scatter(
        claude_representation[i],
        i,
        color=claude_color,
        s=120,
        marker='o',
        zorder=3,
        label='% of Claude\nconversations' if i == 0 else ""
    )
    plt.scatter(
        us_workers_representation[i],
        i,
        color=us_workers_color,
        s=120,
        marker='o',
        zorder=2,
        label='% of U.S.\nworkers' if i == 0 else ""
    )
    
    left_label_offset = 0.6
    right_label_offset = 0.6
    font_size = 11.5
    if claude_representation[i] > us_workers_representation[i]:
        plt.text(
            claude_representation[i] + right_label_offset,
            i,
            f"{claude_representation[i]:.1f}%",
            color=claude_color,
            va='center',
            fontsize=font_size,
            family='DejaVu Sans'
        )
        plt.text(
            us_workers_representation[i] - left_label_offset,
            i,
            f"{us_workers_representation[i]:.1f}%",
            color=us_workers_color,
            va='center',
            fontsize=font_size,
            ha='right',
            family='DejaVu Sans'
        )
    else:
        plt.text(
            us_workers_representation[i] + right_label_offset,
            i,
            f"{us_workers_representation[i]:.1f}%",
            color=us_workers_color,
            va='center',
            fontsize=font_size,
            family='DejaVu Sans'
        )
        plt.text(
            claude_representation[i] - left_label_offset,
            i,
            f"{claude_representation[i]:.1f}%",
            color=claude_color,
            va='center',
            fontsize=font_size,
            ha='right',
            family='DejaVu Sans'
        )

plt.xlabel('Representation relative to US economy', fontsize=12, fontweight='bold', family='DejaVu Sans', labelpad=20)
plt.xticks([0, 10, 20, 30, 40], ['0%', '10%', '20%', '30%', '40%'], fontsize=10, family='DejaVu Sans')
plt.yticks(range(len(categories)), categories, fontsize=10, family='DejaVu Sans', ha='right')

plt.gca().tick_params(axis='x', which='both', direction='out', length=5, pad=5, width=2)
plt.gca().tick_params(axis='y', which='both', length=0, pad=15)
plt.gca().spines['bottom'].set_linewidth(2)
plt.gca().spines['left'].set_linewidth(2)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.gca().grid(False)
plt.gca().grid(axis='x', linestyle=(0, (2, 2)), color='grey', lw=2.5, alpha=0.3)

plt.xlim(-5, 45)

legend = plt.legend(
    loc='lower right',
    bbox_to_anchor=(1, 0.05),
    prop={'family': 'DejaVu Sans', 'size': 12},
    markerscale=2.5,
    handletextpad=1.2,
    labelspacing=1.5,
    borderpad=1.2
)
legend.get_frame().set_linewidth(2)

plt.gca().invert_yaxis()

plt.subplots_adjust(top=0.9, bottom=0.1, left=0.4, right=0.9)
plt.suptitle("AI usage by job type", fontsize=20, fontweight='bold')
plt.show()
