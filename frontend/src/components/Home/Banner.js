import React, { useState } from "react";


const Banner = () => {
  const [isSearchBoxVisible, setIsSearchBoxVisible] = useState(false);

  const showSearchBox = (event) => {
    setIsSearchBoxVisible(!isSearchBoxVisible);
  };
  return (
    <div className="banner text-white">
      <div className="container p-4 text-center">
        <img src={logo} alt="banner" />
        <div>
          <span id="get-part" onClick={showSearchBox}>
            A place to get
          </span>
          {isSearchBoxVisible && <SearchBox />}
        </div>
      </div>
    </div>
  );
};

export default Banner;
