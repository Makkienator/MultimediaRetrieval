# Copyright 2022 Cristian Grosu
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# (a) Find out what is the average shape in the database (in terms of vertex and face counts);
# (b) If there are significant outliers from this average (e.g. shapes having many, or few, vertices or cells).
# The best way to do this is to show a histogram counting how many shapes are in the database for every range of the property of interest 
# (e.g., number of vertices, number of faces, shape class).


import matplotlib.pyplot as plt


def plot_histogram(data, by = "vertices_count"):
    plt.hist(data)
    plt.title(f"Histogram of {by}")    
    plt.show()

