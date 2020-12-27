import React from 'react';
import {Line} from "react-chartjs-2";

const Category = (props) => {

    const categories = props.dataCat
    let labels = []
    let views = []

    {
        categories.map(r => (
            labels.push(r.category),
                views.push(r.views)
                // console.log(r)
        ))
    }
    // const labelsFilter = [...new Set(labels)]

    const colors = ['red', 'blue', 'orange', 'green', 'pink', 'yellow', 'violet', 'black', 'teal', 'grey']

    const state = {
        labels: labels,
        datasets: [
            {
                label: 'Distribution by Category',
                fill: false,
                border: 1,
                borderColor: 'brown',
                backgroundColor: colors,
                data: views,
                options: {}
            },
        ]
    }
    return (
        <div className='container mt-2' style={{minWidth: "80rem"}}>
            <h4 className='mt-3 border-top border-bottom'>Distribution by Category</h4>
            <div className="">
                <Line
                    data={state}
                    width={100}
                    height={250}
                    options={{
                        maintainAspectRatio: false,
                        legend: {
                            display: false,
                            label: {
                                fontSize:16
                            }
                        },
                        scales: {
                            xAxes: [{
                                ticks: {
                                    autoSkip: false,
                                    maxRotation: 90,
                                    minRotation: 90
                                }
                            }]
                        }
                    }}
                />
            </div>
        </div>
    );
};

export default Category;