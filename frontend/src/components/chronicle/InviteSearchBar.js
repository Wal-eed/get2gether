import React, { useState } from 'react'
import './SearchField.scss';
import {
    Grid
} from "@material-ui/core";
import Contact from './Contact';

const InviteSearchBar = ({ startNewMeeting }) => {
    const [query, setQuery] = useState("");
    return (
        <div style={{ display: "block", margin: "50px auto" }}>
            <input class="c-checkbox" type="checkbox" id="checkbox" />
            <div class="c-formContainer" style={{ margin: "0 auto" }}>
                <form class="c-form" onSubmit={startNewMeeting}>
                    <input class="c-form__input" name="contactName" value={query} onChange={(e) => setQuery(e.target.value)} defaultValue={query} placeholder="John Smith" />
                    <button type="submit" class="c-form__button">></button>
                    <label class="c-form__toggle" for="checkbox" data-title="Add From Contacts"></label>
                </form>
            </div>
            {(query !== "") && (
                <Grid container>
                    <Grid item xs={6}>
                        <Contact 
                            image="https://t4.ftcdn.net/jpg/02/14/74/61/360_F_214746128_31JkeaP6rU0NzzzdFC4khGkmqc8noe6h.jpg"
                            name="Jason Smith"
                            bio="I love Pizza. Please invite me to pizza dinners!"
                        />
                    </Grid>
                    <Grid item xs={6}>
                        <Contact 
                            image="https://img.buzzfeed.com/buzzfeed-static/static/2015-05/20/13/campaign_images/webdr01/what-your-favorite-stock-photo-spaghetti-person-s-2-7471-1432142821-2_dblbig.jpg?resize=1200:*"
                            name="Jane Smith"
                            bio="Noodles are life. Also I hate JavaScript"
                        />
                    </Grid>
                </Grid>
            )}
        </div>
    );
}

export default InviteSearchBar;
