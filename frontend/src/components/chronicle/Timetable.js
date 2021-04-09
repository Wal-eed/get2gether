import React, { useState } from 'react'
import PropTypes from 'prop-types'
import './Timetable.scss';

const days = [
    "",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
];

const times = [
    "12:00 am",
    "1:00 am",
    "2:00 am",
    "3:00 am",
    "4:00 am",
    "5:00 am",
    "6:00 am",
    "7:00 am",
    "8:00 am",
    "9:00 am",
    "10:00 am",
    "11:00 am",
    "12:00 pm",
    "1:00 pm",
    "2:00 pm",
    "3:00 pm",
    "4:00 pm",
    "5:00 pm",
    "6:00 pm",
    "7:00 pm",
    "8:00 pm",
    "9:00 pm",
    "10:00 pm",
    "11:00 pm"
];



const Timetable = props => {
    const [isMouseDown, setIsMouseDown] = useState(false);

    let timeMatrix = [];
    for (let i = 0; i < times.length; i++) {
        timeMatrix[i] = new Array(days.length);
    }
    const [schedule, setSchedule] = useState(timeMatrix);

    const handleSelectTime = (row, col, force=false) => {
        if (isMouseDown || force) {
            console.log("Selecting!!!" + row + " " + col);
            let newTimeMatrix = [];
            for (let i = 0; i < times.length; i++) {
                newTimeMatrix[i] = [...schedule[i]];            
            }
            newTimeMatrix[row][col] = (newTimeMatrix[row][col]) ? (0) : (1);
            setSchedule(newTimeMatrix);
        }
    };

    return (
        <div>
            <div>
                <table onMouseDown={() => setIsMouseDown(true)} onMouseUp={() => setIsMouseDown(false)}>
                    <thead>
                        <tr>
                            {days.map(eachField => (
                                <th className="noselect">
                                    {eachField}
                                </th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {times.map((eachTime, row) => (
                            <tr>
                                <td className="noselect">
                                    {eachTime}
                                </td>
                                {days.map((_, col) => {
                                    if (col !== 0) {
                                        return (
                                            <td 
                                                // id={`time-${row}-${col}`} 
                                                className={`time-brick noselect ${schedule[row][col] && "time-brick-selected"}`} 
                                                onMouseOver={() => handleSelectTime(row, col)}
                                                onMouseDown={() => handleSelectTime(row, col, true)}
                                            >
                                            </td>
                                        );
                                    }
                                })}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    )
}

Timetable.propTypes = {

}

export default Timetable
