import React, { useState } from 'react'
import PropTypes from 'prop-types'
import './Timetable.scss';
import Button from '../elements/Button';

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

const saveNewEventSchedule = (schedule) => {
    window.localStorage.setItem("schedule", JSON.stringify(schedule));
}

const overlayThisSchedule = (schedule) => {
    const oldSchedule = JSON.parse(window.localStorage.getItem("schedule"));
    for (let i = 0; i < times.length; i++) {
        for (let j = 0; j < days.length; j++) {
            oldSchedule[i][j] += schedule[i][j];
        }
    }
    window.localStorage.setItem("schedule", JSON.stringify(oldSchedule));
}

const Timetable = ({ isOrganiser, defaultSchedule, participants=5, showLegend, modifiable=true, allowAutofill=false }) => {
    const [isMouseDown, setIsMouseDown] = useState(false);

    
    let timeMatrix = [];
    for (let i = 0; i < times.length; i++) {
        timeMatrix[i] = new Array(days.length);
        for (let j = 0; j < days.length; j++) {
            timeMatrix[i][j] = 0;
        }
    }

    const unitHue = 255 / participants;
    console.log(unitHue);
    const hues = [];
    const opacities = [];
    for (let i = 0; i <= participants; i++) {
        hues.push(i * unitHue);
        opacities.push(1);
    }
    opacities[0] = 0.2;
    console.log(hues);

    let autofillUnblockedSchedule = [];
    for (let i = 0; i < times.length; i++) {
        autofillUnblockedSchedule[i] = new Array(days.length);
        for (let j = 0; j < days.length; j++) {
            autofillUnblockedSchedule[i][j] = 0;
        }
    }

    // POV: You are blocked on monday, tuesday, wednesday for these times:
    // Monday 
    autofillUnblockedSchedule[6][1] = 1;
    autofillUnblockedSchedule[7][1] = 1;
    autofillUnblockedSchedule[8][1] = 1;
    autofillUnblockedSchedule[9][1] = 1;
    autofillUnblockedSchedule[10][1] = 1;
    autofillUnblockedSchedule[11][1] = 1;
    autofillUnblockedSchedule[12][1] = 1;
    // Tuesday 
    autofillUnblockedSchedule[11][2] = 1;
    autofillUnblockedSchedule[12][2] = 1;
    autofillUnblockedSchedule[13][2] = 1;
    autofillUnblockedSchedule[14][2] = 1;
    autofillUnblockedSchedule[15][2] = 1;
    autofillUnblockedSchedule[16][2] = 1;
    autofillUnblockedSchedule[17][2] = 1;
    // Wednesday
    autofillUnblockedSchedule[11][3] = 1;
    autofillUnblockedSchedule[12][3] = 1;
    autofillUnblockedSchedule[13][3] = 1;
    autofillUnblockedSchedule[14][3] = 1;
    autofillUnblockedSchedule[15][3] = 1;
    autofillUnblockedSchedule[16][3] = 1;
    autofillUnblockedSchedule[17][3] = 1;

    const autofill = () => {
        for (let i = 0; i < times.length; i++) {
            for (let j = 0; j < days.length; ++j) {
                if (autofillUnblockedSchedule[i][j]) {
                    // This time is blocked. Do not add
                    schedule[i][j] = 0;
                } else {
                    schedule[i][j] = 1;
                }
            }
        }
        setSchedule([...schedule]);
    }


    const [schedule, setSchedule] = useState(defaultSchedule ? defaultSchedule : timeMatrix);

    const handleSelectTime = (row, col, force=false) => {
        if (modifiable) {
            if (isMouseDown || force) {
                let newTimeMatrix = [];
                for (let i = 0; i < times.length; i++) {
                    newTimeMatrix[i] = [...schedule[i]];            
                }
                newTimeMatrix[row][col] = (newTimeMatrix[row][col]) ? (0) : (1);
                setSchedule(newTimeMatrix);
                if (isOrganiser) {
                    saveNewEventSchedule(newTimeMatrix);
                }
            }
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
                                        // if (schedule[row][col]) console.log("1");
                                        // console.log(schedule[row][col]);
                                        return (
                                            <td 
                                                // id={`time-${row}-${col}`} 
                                                className={`time-brick noselect ${schedule[row][col] && "time-brick-selected"}`} 
                                                style={
                                                    (!modifiable) ? ({
                                                        backgroundColor: `rgba(0, 0, ${hues[schedule[row][col]]}, ${opacities[schedule[row][col]]})`
                                                    }) : ({})
                                                }
                                                onMouseOver={() => handleSelectTime(row, col)}
                                                onMouseDown={() => handleSelectTime(row, col, true)}
                                            >
                                                {schedule[row][col]}
                                            </td>
                                        );
                                    }
                                })}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
            {allowAutofill && (
                <>
                    <Button color="primary" onClick={autofill}>Auto-Fill</Button> 
                    <Button color="info" onClick={() => overlayThisSchedule(schedule)}>Save</Button> 
                </>
            )}
            {showLegend && (
                <div>
                    <h4 style={{textAlign: "left"}}>
                        Legend:
                    </h4>
                    <div style={{width: (participants * 40) + "px", backgroundColor: "whitesmoke", height: "40px", borderRadius: "10px"}}>
                        {Array.from(Array(participants).keys()).map(i => {
                            return (
                                <div style={{display: "inline-block", width: "32px", margin: "4px", height: "30px", backgroundColor: `rgb(0, 0, ${hues[i]})`, borderRadius: "10px"}}>
                                    {i+1}/{participants}
                                </div>
                            )
                        })}
                    </div>
                </div>
            )}
        </div>
    )
}

Timetable.propTypes = {

}

export default Timetable
