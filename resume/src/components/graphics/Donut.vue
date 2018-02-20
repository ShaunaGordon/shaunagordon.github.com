<template>
  <div :id="id">

  </div>
</template>

<script>
import * as d3 from 'd3';

export default {
    props: [
        'name',
        'items'
    ],
    computed: {
        id() {
            return `skill-${this.name}`
        }
    },
    methods: {
        createD3DataSet() {
            let names = Object.keys(this.items);
            return names.map((name, index) => {
                return {
                    index: index,
                    name: name,
                    years: this.items[name]
                }
            });
        },
        createChart() {
            let dataset = this.createD3DataSet();
            let format = d3.format('%');

            let pie = d3.pie()
                .value(d => d.years)
                .sort(null)
                .padAngle(.01);

            let w = 400, h = 400;
            let canvasWidth = w * 1.1, canvasHeight = h * 1.1;
            let donutWidth = 50;
            let radius = Math.min(w/1.5, h) / 2;

            let color = d3.scaleSequential(d3.interpolateViridis);

            let arc = d3.arc()
                    .innerRadius(radius - donutWidth)
                    .outerRadius(radius);

            let outerArc = d3.arc()
                    .innerRadius(radius * 1.23)
                    .outerRadius(radius * 1.23);

            let zoomArc = d3.arc()
                    .innerRadius((radius - donutWidth) * 1.1)
                    .outerRadius(radius * 1.2);

            let svg = d3.select(`#${this.id}`)
                        .append("svg")
                        .attr('width', canvasWidth)
                        .attr('height', canvasHeight);

            svg.append('g').attr('class', 'slices').attr('transform', 'translate('+canvasWidth/2+','+canvasHeight/2+')');
            svg.append('g').attr('class', 'labels').attr('transform', 'translate('+canvasWidth/2+','+canvasHeight/2+')');
            svg.append('g').attr('class', 'lines').attr('transform', 'translate('+canvasWidth/2+','+canvasHeight/2+')');
            svg.append('g').attr('class', 'name').attr('transform', 'translate('+canvasWidth/2+','+canvasHeight/2+')');

            let path = svg.select('.slices').selectAll('.slice')
                    .data(pie(dataset))
                    .enter()
                    .append('path')
                        .attr('id', (d,i) => `slice-${d.data.name}-${i}`)
                        .attr('class', 'slice')
                        .attr('d', arc)
                        .attr('fill', (d,i) => color(d.data.name.length * (d.data.index + 1) * d.data.years * 0.005))
                        .on('mouseenter', function(d) {
                            d3.select(this)
                                .transition()
                                .duration(1000)
                                .attr('d', zoomArc);
                        })
                        .on('mouseleave', function(d) {
                            d3.select(this)
                                .transition()
                                .duration(1000)
                                .attr('d', arc);
                        });

            let outerPath = svg.select('.labels').selectAll('.path')
                        .data(pie(dataset))
                        .enter()
                        .append('path')
                        .attr('id', (d,i) => `label-${d.data.name}-${i}`)
                        .attr('d', outerArc)
                        .attr('class', 'path');

            let labels = svg.select('.slices').selectAll('.label')
                    .data(pie(dataset))
                    .enter()
                        .append('text')
                            .attr('class', 'label')
                            .attr('transform', (d) => "translate(" + outerArc.centroid(d) + ")")
                            .attr('text-anchor', 'middle')
                            .text((d) => d.data.name);

            let skillLabel = svg.select('.name')
                        .append('text')
                            .attr('class', 'name')
                            .attr('text-anchor', 'middle')
                            .text(this.name);
        }
    },
    mounted() {
        this.createChart();
    }
}
</script>

<style>
    svg {
        font-size: 1.1rem;
    }

    .slice {
        transition: all 1s;
    }
</style>
