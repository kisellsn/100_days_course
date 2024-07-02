import pandas

squirrel_data = pandas.read_csv(
    "2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240702.csv"
    )

# squirrel_count = {}
# for index, row in squirrel_data.iterrows():
#     if row["Primary Fur Color"] not in squirrel_count:
#         squirrel_count[row["Primary Fur Color"]] = 1
#     else:
#         squirrel_count[row["Primary Fur Color"]] += 1
# squirrel_count_csv = pandas.DataFrame({
#     "fur color": list(squirrel_count.keys()),
#     "count": list(squirrel_count.values())
# })


# squirrel_count_csv.to_csv("squirrel_count_csv.csv")

gray_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_count_csv = pandas.DataFrame({
    "fur color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
})

squirrel_count_csv.to_csv("squirrel_count_csv.csv")