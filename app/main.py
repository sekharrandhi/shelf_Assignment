from flask import Flask, request, jsonify

app = Flask(__name__)


# def identify_shape(shelf_layout):
#     # Initialize a dictionary to store the result
#     result = {}
#
#     # Define the symbols for each brand
#     symbols = {'G': 'Good Day', 'M': 'Marie Gold', 'N': 'NutriChoice', 'B': 'Milk Bikis'}
#
#     for symbol in symbols:
#         # Initialize variables to track the coordinates of the symbol
#         min_row, max_row, min_col, max_col = float('inf'), -1, float('inf'), -1
#
#         # Iterate through the shelf layout to find the symbol's coordinates
#         for i, row in enumerate(shelf_layout):
#             for j, product in enumerate(row):
#                 if product == symbol:
#                     min_row = min(min_row, i)
#                     max_row = max(max_row, i)
#                     min_col = min(min_col, j)
#                     max_col = max(max_col, j)
#
#         # Calculate the shape based on the coordinates
#         width = max_col - min_col + 1
#         height = max_row - min_row + 1
#
#         if width == height == 1:
#             shape = 'point'
#         elif width == 1:
#             shape = 'vertical rectangle'
#         elif height == 1:
#             shape = 'horizontal rectangle'
#         elif width == height:
#             shape = 'square'
#         else:
#             shape = 'polygon'
#
#         # Determine the location based on the coordinates
#         location = []
#         if min_row == 0:
#             location.append('top')
#         if max_row == len(shelf_layout) - 1:
#             location.append('bottom')
#         if min_col == 0:
#             location.append('left')
#         if max_col == len(shelf_layout[0]) - 1:
#             location.append('right')
#
#         result[symbols[symbol]] = {'shape': shape, 'location': location}
#
#     return result
def identify_shape(shelf_layout):
    # Initialize a dictionary to store the result
    result = {}

    # Define the symbols for each brand
    symbols = {'G': 'Good Day', 'M': 'Marie Gold', 'N': 'NutriChoice', 'B': 'Bikis'}

    for symbol in symbols:
        # Initialize variables to track the coordinates of the symbol
        min_row, max_row, min_col, max_col = float('inf'), -1, float('inf'), -1

        # Iterate through the shelf layout to find the symbol's coordinates
        for i, row in enumerate(shelf_layout):
            for j, product in enumerate(row):
                if product == symbol:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)

        # Calculate the shape based on the coordinates
        width = max_col - min_col + 1
        height = max_row - min_row + 1

        if width == height == 1:
            shape = 'point'
        elif width == 1:
            shape = 'vertical rectangle'
        elif height == 1:
            shape = 'horizontal rectangle'
        elif width == height:
            shape = 'square'
        else:
            shape = 'polygon'

        # Determine the location based on the coordinates
        location = []
        if min_col == 0:
            location.append('left')
        if max_col == len(shelf_layout[0]) - 1:
            location.append('right')
        if min_row == 0:
            location.append('top')
        if max_row == len(shelf_layout) - 1:
            location.append('bottom')

        result[symbols[symbol]] = {'shape': shape, 'location': location}

    return result



@app.route('/analyze-shelf', methods=['POST'])
def analyze_shelf():
    try:
        data = request.get_json()
        shelf_layout = data.get('shelf_layout')
        if shelf_layout:
            result = identify_shape(shelf_layout)
            return jsonify(result)
        else:
            return jsonify({'error': 'Invalid input format'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

#1.
# {
#   "shelf_layout": [
# ["G", "M", "N", "B"],
# ["G", "M", "N", "B"],
# ["G", "M", "N", "B"],
# ["G", "M", "N", "B"]
#   ]
# }
# 2.
# [
# ['G', 'G', 'M', 'M'],
# ['G', 'G', 'M', 'M'],
# ['B', 'B', 'N', 'N'],
# ['B', 'B', 'N', 'N']
# ]
# 3. {
# "shelf_layout": [
# ["G", "G", "G", "M", "M", "M", "M"],
# ["G", "B", "G", "M", "N", "N", "M"],
# ["G", "G", "G", "B", "B", "N", "N"],
# ["B", "B", "B", "B", "B", "N", "N"]
# ]
# }