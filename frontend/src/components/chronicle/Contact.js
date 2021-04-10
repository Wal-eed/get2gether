import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import FadeIn from 'react-fade-in';

const useStyles = makeStyles({
  root: {
    maxWidth: 345,
  },
});

export default function ImgMediaCard({ image, name, bio }) {
  const classes = useStyles();

  return (
      <FadeIn>
        <Card className={classes.root} style={{margin: "20px"}}>
        <CardActionArea>
            <CardMedia
            component="img"
            height="140"
            image={image}
            title="Jason Smith"
            />
            <CardContent>
            <Typography gutterBottom variant="h5" component="h2" style={{color: "black"}}>
                {name}
            </Typography>
            <Typography variant="body2" color="textSecondary" component="p">
                {bio}
               
            </Typography>
            </CardContent>
        </CardActionArea>
        <CardActions>
            <Button size="small" color="primary">
            Invite
            </Button>
            <Button size="small" color="primary">
            Add to Favourites
            </Button>
        </CardActions>
        </Card>
      </FadeIn>
  );
}