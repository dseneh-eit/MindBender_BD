import React, {Component} from 'react';
import axios from "axios"
import './App.css';
import Home from "./components/app/Home";
import Region from "./components/app/Region";
import Dashboard from "./components/Dashboard";

class App extends Component {
    today = new Date().toDateString()
// const ye = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(d);
// const mo = new Intl.DateTimeFormat('en', { month: 'short' }).format(d);
// const da = new Intl.DateTimeFormat('en', { day: '2-digit' }).format(d);
    intervalID;
    state = {
        date: null,
        dataList: [], dataRegion: [], dataCategory: [],
        dataRegionCategory: [], dataTotal: [], topVal: 0,
        comp: "Home",
        text: `Top 15 Videos With Highest Views`,
        Update: false
    }

    componentDidMount() {
        // setInterval(this.loadData, 3000)
        this.loadData()
        console.log(this.today)
    }

    async loadData() {
        const requestOne = axios.get("/api/list");
        const requestTwo = axios.get("/api/region");
        const requestThree = axios.get("/api/category");
        const requestFour = axios.get("/api/region-category");
        const requestFive = axios.get("/api");

        axios.all([requestOne, requestTwo, requestThree, requestFour, requestFive]).then(axios.spread((...responses) => {
            this.setState({
                dataList: responses[0].data,
                dataRegion: responses[1].data,
                dataCategory: responses[2].data,
                dataRegionCategory: responses[3].data,
                dataTotal: responses[4].data,
                topVal: responses[0].data[0],

            })
            this.startUpdate()
        })).catch(errors => {
            console.log(errors);
        })
    }


    startUpdate = () => {
        this.intervalID = setTimeout(
            this.loadData.bind(this), 8000)
        this.setState({update: true})
    }

    stopUpdate = () => {
        clearInterval(this.intervalID)
        this.setState({update: false})
    }
    changeUpdate = () => {
        if (this.state.update) {
            this.stopUpdate()
        } else {
            this.startUpdate()
        }
    }

    componentWillUnmount() {
        this.stopUpdate()
    }

    render() {
        const Component = () => {
            let Output;
            switch (this.state.comp) {
                case "Home":
                    Output = (<Home data={this.state.data} dataList={this.state.dataList} dataTotal={this.state.dataTotal}
                                    topVal={this.state.topVal}/>)
                    break;
                case "Region":
                    Output = (<Region dataList={this.state.dataRegion}/>)
                    break;
                case "Dashboard":
                    Output = (<Dashboard dataList={this.state.dataRegion} dataCat={this.state.dataCategory}
                                         dataRegCat={this.state.dataRegionCategory}/>)
                    break;
                default:
                    Output = (null)
            }
            return Output;
        }
        return (
            <div className="App">
                <header className="">
                    <div className='container button-header'>
                        <div className="row mb-2">
                            <div className="col-3">
                                <div className="btn btn-danger"
                                     onClick={() => this.setState({
                                         comp: "Home",
                                         text: `Top 15 Videos With Highest Views`
                                     })}>
                                    Top 15
                                </div>
                                <div className="btn btn-secondary"
                                     onClick={() => this.setState({
                                         comp: "Dashboard",
                                         text: `Top Videos Viewed by Region`
                                     })}>
                                    Dashboard
                                </div>
                            </div>
                            <div className="col-6 mb-2">
                                <h2 className='mb-0 font-weight-bolder text-danger'>YouTube Trending Video Analysis</h2>
                                 <h5 className='mt-1 font-weight-bolder text-primary'>
                                     {this.today}
                                 </h5>
                            </div>
                            <div className="col-3">
                                <div
                                    className={`btn btn-sm ${!this.state.update ? 'btn-primary' : 'btn-danger'} float-right`}
                                    onClick={this.changeUpdate}>
                                    {this.state.update ? '◼ Stop Update' : '▶ Get Update'}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <h4 className='mb-2 mt-4 border-top  border-bottom'>{this.state.text}</h4>
                    </div>
                    <Component/>
                </header>
            </div>
        );

    }
}

export default App;

