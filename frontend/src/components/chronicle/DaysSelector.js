import React, { useState } from 'react'
import PropTypes from 'prop-types'
import './DaysSelector.scss';
import { FaChevronCircleRight, FaChevronCircleLeft } from 'react-icons/fa';

const days = [
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri",
    "Sat",
    "Sun",
];


const DaysSelector = props => {
    const [selected, setSelected] = useState(days.map(_ => 0));

    const select = (i) => {
        const newSelections = [...selected];
        newSelections[i] = newSelections[i] ? 0 : 1;
        setSelected(newSelections)
    }

    return (
        <div style={{marginBottom: "50px", marginTop: "50px"}}>
            <div className="chevron" style={{display: "inline-block"}}>
                <FaChevronCircleLeft />
            </div>
            {days.map((eachDay, i) => (
                <div 
                    className={`${selected[i] ? "selected" : "days-selector"}`}
                    style={{
                        display: "inline-block", 
                        color: "black", 
                        margin: "10px", 
                        borderRadius: "10px"
                    }}
                    onClick={() => select(i)}
                >
                    {eachDay}

                </div>
            ))}
            <div style={{display: "inline-block"}}>
                <FaChevronCircleRight />
            </div>
        </div>
    )
}

DaysSelector.propTypes = {

}

export default DaysSelector
