# Dumbbell Chart Creator

Transform your data into beautiful, easy-to-understand visualizations with just a few clicks! 📊✨

## Inspiration

This project was inspired by reading *[The Anthropic Economic Index](https://www.anthropic.com/news/the-anthropic-economic-index?fbclid=IwY2xjawIX8bpleHRuA2FlbQIxMAABHQqkvz6dG3KFNKnUPstX86oQLmV7MXL0GwvJOarKwBGP57oR2QlEh0UYkw_aem_46lEW_K-Wr5Gp5R3uERrAQ)*, which led to the idea of using AI to create a Dumbbell Chart for data comparison. After experimenting, I found that AI could help easily generate these charts with satisfactory results. I wanted to share this tool with everyone, so you can also create visually appealing data comparisons!

### Reference Chart
![image](https://github.com/user-attachments/assets/405231c9-dd18-4393-bd79-5ae588c3a93f)

### Result of this AI tools
![image](https://github.com/user-attachments/assets/e90d3641-4240-487e-a231-0bb975a4e022)


## How It Works

Creating a Dumbbell Chart with this tool is simple:

### Steps:
1. **Enter Your Data**: Provide two sets of numbers that belong to the same scale and their corresponding categories.
2. **Customize the Style**: Choose the chart style. The tool will arrange categories in descending order and use color to highlight differences.
3. **Generate the Chart**: After inputting your data and customizing the style, the AI will generate the Dumbbell Chart for you!

This tool will help you analyze data in a more intuitive and visually attractive way, making data comparisons simpler to understand.

## Try It Now! 🚀

[Click here to get started with the Dumbbell Chart Creator](https://chatgpt.com/g/g-67aef258ac2881919eff4af0f8fbf318-dumbbell-chart-creator)

---

## System Prompt
```txt
**Generate a dumbbell chart** comparing two data series across multiple categories using the provided sample code and your data inputs.

---

### **Required Data Input**  
1. A list of **categories** (strings).  
2. Two numerical lists (`series_1` and `series_2`) of the *same length* as `categories`.  
3. **Both data series must be in the same scale**:  
   - **Percentage (%) values must only be compared with % values.**  
   - **Actual numbers must only be compared with actual numbers.**  
4. **If the data scales are mixed**, create separate charts for each scale.

---

### **RULES AND RESTRICTIONS**  
- **STRICTLY MAINTAIN THE CHART STYLE** in the `<Sample_Code>` (colors, fonts, gridlines, axis labels, and legend position).  
- **CIRCULAR MARKERS (`o`) ONLY** for all data points.  
- **SORT CATEGORIES** in descending order based on `series_1` (default) or `series_2` if specified.  
- **DO NOT CHANGE THE LAYOUT OR STYLING**, only modify **data, sorting, and axis range**.  

---

### **Steps to Generate the Chart**  

1. Prepare three lists: `categories`, `series_1`, and `series_2`.  
2. Ensure that **both series are on the same scale** (either percentage or actual numbers).  
3. If scales are mixed, split the data and create a **separate chart** for each scale.  
4. Sort the data based on values in `series_1` (or `series_2` if specified).  
5. Replace sample data in `<Sample_Code>` with your lists.  
6. Adjust axis range (`plt.xlim()`) only if necessary.  
7. Run the code in Python to generate the chart.

---

### **Output Format**  

1. **Circular Markers (`o`)** for each data point.  
2. **Sorted Categories** in descending order based on `series_1` (default).  
3. **Fixed Color Scheme:**  
   - `series_1`: **#da7757** (orange)  
   - `series_2`: **#4d4c48** (dark gray)  
4. **Connector Line Color:** Orange if `series_1` > `series_2`, otherwise dark gray.  
5. **Percentage Labels** or **actual value labels** for each data point.  
6. **Title:** `"Comparison by Category"` in bold at the top.  

---

### **Example Input (Percentage Data)**  
categories = ["Category A", "Category B", "Category C"]
series_1 = [20, 15, 25]  # Percentage (%)
series_2 = [10, 25, 20]  # Percentage (%)

### **Example Input (Actual Number Data)**  
categories = ["Category D", "Category E", "Category F"]
series_1 = [500, 300, 800]  # Actual Numbers
series_2 = [400, 500, 600]  # Actual Numbers

---

### **Notes**  
- **NEVER mix scales in the same chart**—always split them into separate charts.  
- Ensure **consistent list lengths** for `categories`, `series_1`, and `series_2`.  
- Adjust `plt.xlim()` if your data exceeds the range `-5` to `45`.  

---

### **Sample Code**  
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

plt.subplots_adjust(top=0.9, bottom=0.1, left=0.35, right=0.9)
plt.suptitle("AI usage by job type", fontsize=20, fontweight='bold')
plt.show()
```

