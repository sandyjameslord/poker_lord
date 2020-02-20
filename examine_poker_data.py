import generate_poker_data
import matplotlib.pyplot as plt
import seaborn as sns

poker_data = generate_poker_data.generate_poker_data()

def show_poker_results(poker_data):
    categories = ["tied", "p1", "pl2", "pl3", "pl4", "pl5", "hic_w", "pai_w", "2pa_w", "thr_w", "str_w", "flu_w", "fuh_w", "fou_w", "stf_w"]
    axes = sns.barplot(x=categories, y=poker_data, palette='bright')
    axes.set_title("Playing 5 Card Stud 100,000 Times")
    axes.set(xlabel="Kind of Victory", ylabel="Num Times Won")
    axes.set_ylim(top=max(poker_data)*1.10)
    for bar, datum in zip(axes.patches, poker_data):
        text_x = bar.get_x() + bar.get_width() / 2.0
        text_y = bar.get_height()
        text = f"""{datum:,}\n{(datum / 100_000):.3%}"""
        axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom')
    plt.show(axes)

show_poker_results(poker_data)
