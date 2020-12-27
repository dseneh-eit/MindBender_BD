import React from 'react';
import {Bar, Doughnut} from "react-chartjs-2";

const Region = (props) => {

    const regions = props.dataList
    let labels = []
    let countries = []
    let views = []

    let catViews = []
    //
    {
        regions.map(r => (
            labels.push(r.country),
                views.push(r.views)
        ))
    }
    // console.log(views)
    // console.log(labels)
    // let label = [...new Set(labels)]
    // const getCountry = (country) => {
    //     return regions.filter(r => r.country === country).map(r => r.views)
    // }
    // const catList = ['Sports', 'Music', 'People & Blogs', 'Entertainment', 'Film & Animation',
    //     'Autos & Vehicles', 'Pets & Animals', 'Travel & Events', 'Gaming', 'Comedy',
    //     'News & Politics', 'Howto & Style', 'Science & Technology', 'Education', 'Nonprofits & Activism'
    // ]
    const colors = ['red', 'blue', 'orange', 'green', 'pink', 'yellow', 'violet', 'black', 'teal', 'grey']
    const country = ['USA', 'Germany', 'China', 'Great Britain', 'Russia', 'South Korea', 'Japan', 'India', 'Canada', 'France']

    const state = {
        labels: labels,
        datasets: [
            {
                label: '# of views',
                backgroundColor: colors,
                data: views,
                options: {}

            },
        ]
    }
    return (
        <div >
            <div className="row bg-transparent">
                <div className="col-lg-8">
                    <Bar
                        data={state}
                        width={100}
                        height={300}
                        options={{
                            maintainAspectRatio: false,
                            legend: {
                                display: false,
                            }
                        }}
                    />
                </div>
                <div className="col-lg-4">
                    <Doughnut
                        data={state}
                        width={100}
                        height={300}
                        options={{
                            maintainAspectRatio: false,
                            legend: {
                                display: true,
                                position: 'right'
                            }
                        }}
                    />
                </div>
            </div>


        </div>
    );
};

export default Region;