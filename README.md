<h1>Project Documentation</h1>

<h2>Overview</h2>
<p>
This project provides a solution for travelling salesman problem for 50 cities.
It includes:
</p>
<ul>
  <li>A dataset containing 50 city coordinates.</li>
  <li>A Jupyter Lab workflow for implementing and analyzing algorithms.</li>
  <li>A modular folder structure that separates source code, data, and runtime results.</li>
</ul>
<p>
This document explains how to install Jupyter Lab, set up Python dependencies, and understand the project directory layout.
</p>

<hr>

<h2>Installation Guide</h2>

<h3>1. Install Python</h3>
<p>
Ensure having <strong>Python 3.9 or above</strong> installed. Download Python from:
</p>
<p><a href="https://www.python.org/downloads/">https://www.python.org/downloads/</a></p>

<p>Verify installation:</p>
<pre><code>python --version
</code></pre>

<p>(Optional) Create a virtual environment:</p>
<pre><code>python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
</code></pre>

<h3>2. Install Jupyter Lab</h3>
<pre><code>pip install jupyterlab
</code></pre>

<p>Launch Jupyter Lab:</p>
<pre><code>jupyter lab
</code></pre>

<h3>3. Install Python Packages</h3>

<p>Install the required libraries individually:</p>

<pre><code>pip install pandas
pip install numpy
pip install seaborn
pip install scipy
pip install scikit-learn
pip install ipywidgets
pip install torch
pip install optuna
pip install xgboost
</code></pre>

<p>Or install everything at once using a <code>requirements.txt</code> file:</p>

<pre><code>pip install -r requirements.txt
</code></pre>

<hr>

<h2>Folder Structure</h2>

<pre><code>project-root/
│
├── data/
│   └── cities.csv
│
├── src/
│   └── AI_for_search_and_optimization_final_Coursework_25043636.ipynb
│
├── results/
│   └── (runtime-generated outputs)
│
└── README.md
</code></pre>

<h3>data/</h3>
<p>Stores all raw datasets. Contains <code>cities.csv</code> with 50 coordinate pairs used as input for optimization tasks.</p>

<h3>src/</h3>
<p>Contains source code and notebooks. Includes <code>AI_for_search_and_optimization_final_Coursework_25043636.ipynb</code>, the primary notebook for running algorithms and experiments.</p>

<h3>results/</h3>
<p>Holds all runtime-generated outputs, including:</p>
<ul>
  <li>City Routes</li>
  <li>Current vs Best Distance</li>
  <li>Tables</li>
  <li>Optimization results</li>
</ul>

<hr>

<h2>How to Run the Project</h2>

<ol>
  <li>Install the required dependencies.</li>
  <li>Open a terminal in the project root.</li>
  <li>Launch Jupyter Lab:
    <pre><code>jupyter lab</code></pre>
  </li>
  <li>Open <code>src/main.ipynb</code>.</li>
  <li>Ensure <code>data/cities.csv</code> is present.</li>
  <li>Run the notebook to generate outputs in the <code>results/</code> folder.</li>
</ol>

<hr>

<h2>Support</h2>
<p>
For issues, improvements, or questions, please email or open an issue in Github.
</p>
