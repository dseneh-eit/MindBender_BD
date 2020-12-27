import React from 'react';
import Region from "./app/Region";
import Category from "./app/Category";

const Dashboard = (props) => {
    return (
        <div className='container mt-2' style={{minWidth: "80rem"}}>
            <div>
                <Region dataList={props.dataList} />
            </div>
            <div>
                <Category dataList={props.dataRegCat} dataCat={props.dataCat} />
            </div>
        </div>
    );
};

export default Dashboard;
