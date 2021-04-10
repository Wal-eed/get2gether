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

export default function RangeSlider({ startTimeIndex, setTimerange, endTimeIndex, adjustTimeRange }) {
  const classes = useStyles();
  const [value, setValue] = React.useState([startTimeIndex, endTimeIndex]);

  const handleChange = (event, newValue) => {
    setValue(newValue);
    adjustTimeRange(newValue[0], newValue[1]);
  };

  return (
    <div className={classes.root} style={{display: "inline-block", width: "500px"}}>
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