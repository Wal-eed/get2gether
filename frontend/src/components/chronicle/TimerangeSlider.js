import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Slider from '@material-ui/core/Slider';

const useStyles = makeStyles({
  root: {
    width: 300,
  },
});

function valuetext(value) {
  return `${value}°C`;
}

export default function RangeSlider({ startTimeIndex, setStartTime, endTimeIndex, setEndTime, adjustTimeRange }) {
  const classes = useStyles();
  const [value, setValue] = React.useState([startTimeIndex, endTimeIndex]);

  const handleChange = (event, newValue) => {
    setValue(newValue);
    setStartTime(newValue[0]);
    setEndTime(newValue[1]);
    adjustTimeRange();
  };

  return (
    <div className={classes.root} style={{display: "inline-block"}}>
      <Typography id="range-slider" gutterBottom>
        Time range
      </Typography>
      <Slider
        value={value}
        onChange={handleChange}
        valueLabelDisplay="auto"
        aria-labelledby="range-slider"
        step={1}
        marks
        min={0}
        max={23}
        getAriaValueText={valuetext}
      />
    </div>
  );
}