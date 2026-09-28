import matplotlib.pyplot as plt

# Define your data variables
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9]
exam_scores   = [55, 60, 68, 72, 80, 85, 90, 93, 98]

# Create the scatterplot
plt.scatter(hours_studied, exam_scores, color='purple', s=100)

# Add titles and labels
plt.title('Relationship Between Study Hours and Exam Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')

# Display the plot
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
