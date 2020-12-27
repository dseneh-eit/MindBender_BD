import React, {useEffect, useState} from 'react';
import {Container, ProgressBar, Table} from "react-bootstrap";

const Home = (props) => {
const datalist = props.dataList
  let total = 0;
if (props.topVal){
  total = props.topVal.view_count;
}


  return (
      <div className="mt-2">
        <div className='container' style={{minWidth: "80rem"}}>
          <Table striped bordered hover variant="dark" size="sm">
            <thead>
            <tr>
              <th>Country</th>
              <th>Time</th>
              <th>Channel</th>
              <th>Title</th>
              <th>Category</th>
              <th colSpan={2}>Views</th>
              <th>Likes</th>
              <th>DisLikes</th>
              <th>Comments</th>
            </tr>
            </thead>
            <tbody>

            {datalist.map(data => (
                <tr className='text-left'key={data.id}>
                  <td>{data.country}</td>
                  <td>{data.pub_time}</td>
                  <td >{data.channel_title}</td>
                  <td>{data.video_title.substring(0,25)}...</td>
                  <td>{data.category}</td>
                  <td className='text-center'>{data.view_count.toLocaleString()}</td>
                  <td style={{width: '5%'}}>
                    <div className='progress-bar bg-warning text-warning' style={{width: `${(data.view_count/total)*100}%`}}>
                      {`${Math.round((data.view_count/total)*100)}%`}
                    </div>
                  </td>
                  <td className='text-center'>{data.like_count === null ? 0 :data.like_count.toLocaleString()}</td>
                  <td className='text-center'>{data.dislike_count === null ? 0 :data.dislike_count.toLocaleString()}</td>
                  <td className='text-center'>{data.comment_count === null ? 0 :data.comment_count.toLocaleString()}</td>
                </tr>
            ))}
            </tbody>
          </Table>
        </div>
      </div>
  );
};

export default Home;
