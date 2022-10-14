from mainFunctions.visualize import visualize
from helper.mockDataVisualize import transfer_function_output_ranking

# sentences means list of document sentences
# highlights means list of most important ones

ranking_input = transfer_function_output_ranking(sentences, highlights)
visualize("name_of_the_file Bold", ranking_input, 1)
visualize("name_of_the_file Bold Strong", ranking_input, 2)
visualize("name_of_the_file colors", ranking_input, 3)
visualize("name_of_the_file sizes", ranking_input, 4)
visualize("name_of_the_file sizes 2", ranking_input, 5)