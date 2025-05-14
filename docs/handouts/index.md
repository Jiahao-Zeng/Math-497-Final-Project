---
layout: handouts
title: Course Handouts
---

<h2 class="major">Course Handouts</h2>

<div class="handout-list">
    <div class="handout-item">
        <h3><a href="{{ '/handouts/handout1.html' | relative_url }}">Handout 1: Three-Point Difference Method</a></h3>
        <p>Learn about the three-point difference method for approximating derivatives.</p>
    </div>

    <div class="handout-item">
        <h3><a href="{{ '/handouts/handout2.html' | relative_url }}">Handout 2: Numerical Methods</a></h3>
        <p>Explore second derivative approximations and differential equations.</p>
    </div>

    <div class="handout-item">
        <h3><a href="{{ '/handouts/handout3.html' | relative_url }}">Handout 3: Differential Equations</a></h3>
        <p>Study the traffic flow model and density calculations.</p>
    </div>

    <div class="handout-item">
        <h3><a href="{{ '/handouts/handout4.html' | relative_url }}">Handout 4: Implementation Guide</a></h3>
        <p>Learn about density computations and the upwind scheme.</p>
    </div>

    <div class="handout-item">
        <h3><a href="{{ '/handouts/handout5.html' | relative_url }}">Handout 5: Analysis Techniques</a></h3>
        <p>Advanced analysis of the upwind scheme and error calculations.</p>
    </div>

    <div class="handout-item">
        <h3><a href="{{ '/handouts/handout6.html' | relative_url }}">Handout 6: Final Project Guidelines</a></h3>
        <p>Final project requirements and traffic flow model implementation.</p>
    </div>
</div>

<style>
.handout-list {
    display: grid;
    gap: 2rem;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}
.handout-item {
    background: rgba(255, 255, 255, 0.05);
    padding: 1.5rem;
    border-radius: 4px;
    transition: background-color 0.2s ease;
}
.handout-item:hover {
    background: rgba(255, 255, 255, 0.1);
}
.handout-item h3 {
    margin: 0 0 1rem 0;
    font-size: 1.25em;
}
.handout-item h3 a {
    border: none;
    color: #ffffff;
}
.handout-item p {
    margin: 0;
    font-size: 0.9em;
    opacity: 0.7;
}
</style>