<template>
  <div>
    <div class="home">
      <vue-canvas-nest :config="{color:'255,0,0', count: 350}" :el="'#area'">
      </vue-canvas-nest>
      <div id="area" class="background"></div>
    </div>
    <div class="home">
      <vue-canvas-nest :config="{color:'106,90,205', count: 350}" :el="'#area2'">
      </vue-canvas-nest>
      <div id="area2" class="background2"></div>
    </div>
    <div class="home">
      <vue-canvas-nest :config="{color:'10,255,0', count: 350}" :el="'#area3'">
      </vue-canvas-nest>
      <div id="area3" class="background3"></div>
    </div>
    <div class="home">
      <vue-canvas-nest :config="{color:'255,255,0', count: 350}" :el="'#area5'">
      </vue-canvas-nest>
      <div id="area5" class="background5"></div>
    </div>
    <div class="home">
      <vue-canvas-nest :config="{color:'255,2,255', count: 350}" :el="'#area4'">
      </vue-canvas-nest>
      <div id="area4" class="background4"></div>
    </div>
    <div class="home">
      <vue-canvas-nest :config="{color:'238,99,99', count: 350}" :el="'#area6'">
      </vue-canvas-nest>
      <div id="area6" class="background6"></div>
    </div>
    <div class="webicon">
           LDM
    </div>
    <el-button @click="handleCli" class="show_button"></el-button>
    <div :class = "{intro : ifSelect === 0, intro2:ifSelect === 1}">
      <el-collapse v-model="activeName" accordion>
        <el-collapse-item title="Introduction" name="1" class="step">
          <div>
            <ul>
              <li>
                Because the signal of satellite positioning technology reaches the ground weakly and cannot penetrate buildings, it is impossible to use GPS for accurate positioning in indoor environment.
                At present, Wi Fi based positioning is a popular indoor positioning technology. Its basic positioning methods are signal strength based propagation model method and fingerprint identification method.
                This technology is suitable for positioning and navigation of people / vehicles, medical institutions, shopping malls, theme parks and other scenes that need positioning accuracy at the meter level.
                Android app lzwhr is based on Wi Fi location technology fingerprint method and combined with a variety of improved methods for indoor location. A software is designed for campus users, which is convenient
                for users to find nearby students to chat and make friends, expand the scope of communication, and realize classroom navigation in the teaching building and recommend nearby facilities. The app is mainly
                used in various teaching buildings on the campus, and the target population is students and teachers on the campus. The app aims to help students get around the campus without being familiar with the campus,
                find high-quality self-study rooms, self-help vending machines, offices and other campus logo buildings, and facilitate students' social functions such as making friends, studying together with strangers and meeting new partners on campus.
              </li>
              <li>
                <b>As the DM module of the app, this website is based on the scalability of the software. Provide a developer port. With only one developer account, you can participate in the design of indoor positioning of the software.
                  You can develop a new floor and update the fingerprint information of the existing floor. In this way, everyone can share your creative achievements! Strive to create a better tomorrow!
                  This website also provides monitor port, which can monitor user access records.</b>
              </li>
            </ul>
          </div>
        </el-collapse-item>
        <el-collapse-item title="Features" name="2" class="step">
          <ul>
            <li>
              ...
            </li>
            <li>
              ...
            </li>
            <li>
              ...
            </li>
          </ul>
        </el-collapse-item>
        <el-collapse-item title="How to use" name="3" class="step">
          <div>
            <ul>
              <li>...</li>
              <li>...</li>
              <li>...</li>
              <li>...</li>
            </ul>
          </div>
        </el-collapse-item>
        <el-collapse-item title="How to cite" name="4" class="step">
          <div>...</div>
        </el-collapse-item>
      </el-collapse>
    </div>
    <div class="block">
      <el-carousel height="650px">
        <el-carousel-item v-for="item in imgs" :key="item" class="el-carousel__item">
          <img class="carousel-image" :src="item"/>
        </el-carousel-item>
      </el-carousel>
    </div>
    <div class="block2">
      <el-carousel height="300px">
        <el-carousel-item v-for="item in imgs2" :key="item" class="el-carousel__item">
          <img class="carousel-image" :src="item"/>
        </el-carousel-item>
      </el-carousel>
    </div>
    <div class="block3">
      <el-carousel height="300px">
        <el-carousel-item v-for="item in imgs3" :key="item" class="el-carousel__item">
          <img class="carousel-image" :src="item"/>
        </el-carousel-item>
      </el-carousel>
    </div>
    <div>
      <el-row>
<!--        <el-button round class="log_in_button">登录</el-button>-->
        <el-button round class="register_button">注册</el-button>
      </el-row>
    </div>
  </div>
</template>

<script>
import indexImg1 from '../assets/index_img1.png'
import indexImg11 from '../assets/index_img1_1.png'
import indexImg12 from '../assets/index_img1_2.png'
import indexImg2 from '../assets/index_img2.png'
import indexImg3 from '../assets/index_img3.png'
import indexImg4 from '../assets/index_img4.png'
// import indexImg5 from '../assets/index_img5.png'
import vueCanvasNest from 'vue-canvas-nest'

export default {
  name: 'Index',
  data () {
    return {
      imgs: [indexImg4, indexImg2, indexImg3],
      imgs2: [indexImg1, indexImg11, indexImg12],
      imgs3: [indexImg1, indexImg11, indexImg12],
      activeName: '1',
      ifSelect: 0
    }
  },
  components: {vueCanvasNest},
  methods: {
    handleCli () {
      if (this.ifSelect === 0) {
        this.ifSelect = 1
        console.log(this.ifSelect)
      } else {
        this.ifSelect = 0
        console.log(this.ifSelect)
      }
    }
  }
  // components:{vueCanvasNest}
  // mounted () {
  //   const s = document.createElement('script')
  //   s.type = 'text/JavaScript'
  //   s.src = '../../assets/rvn.js'
  //   document.body.appendChild(s)
  // }
}

// // eslint-disable-next-line no-undef
// particlesJS('particles-js', {
//   particles: {
//     number: {
//       value: 80,
//       density: {
//         enable: true,
//         value_area: 800
//       }
//     },
//     color: {
//       value: ['#2EB67D', '#ECB22E', '#E01E5B', '#36C5F0']
//     },
//     shape: {
//       type: ['circle'],
//       stroke: {
//         width: 0,
//         color: '#fff'
//       },
//       polygon: {
//         nb_sides: 5
//       }
//     },
//     opacity: {
//       value: 1,
//       random: false,
//       anim: {
//         enable: false,
//         speed: 1,
//         opacity_min: 0.1,
//         sync: false
//       }
//     },
//     size: {
//       value: 8,
//       random: true,
//       anim: {
//         enable: false,
//         speed: 10,
//         size_min: 10,
//         sync: false
//       }
//     },
//     line_linked: {
//       enable: true,
//       distance: 150,
//       color: '#808080',
//       opacity: 0.4,
//       width: 1
//     },
//     move: {
//       enable: true,
//       speed: 5,
//       direction: 'none',
//       random: false,
//       straight: false,
//       out_mode: 'out',
//       bounce: false,
//       attract: {
//         enable: false,
//         rotateX: 600,
//         rotateY: 1200
//       }
//     }
//   },
//   interactivity: {
//     detect_on: 'canvas',
//     events: {
//       onhover: {
//         enable: true,
//         mode: 'grab'
//       },
//       onclick: {
//         enable: true,
//         mode: 'push'
//       },
//       resize: true
//     },
//     modes: {
//       grab: {
//         distance: 140,
//         line_linked: {
//           opacity: 1
//         }
//       },
//       bubble: {
//         distance: 400,
//         size: 40,
//         duration: 2,
//         opacity: 8,
//         speed: 3
//       },
//       repulse: {
//         distance: 200,
//         duration: 0.4
//       },
//       push: {
//         particles_nb: 4
//       },
//       remove: {
//         particles_nb: 2
//       }
//     }
//   },
//   retina_detect: true
// })

</script>

<style>
.show_button{
  z-index: 500;
  background: transparent;
  position: absolute;
  left: 175px;
  top: 213px;
  heignt: 15px;
  width: 15px;
}

.register_button{
  position:absolute;
  top: 200px;
  left: 1600px;
}

.block {
  height: 800px;
  width: 500px;
  position: absolute;
  left: 930px;
  top: 200px;
  z-index: 1000;
}
.block2 {
  height: 800px;
  width: 500px;
  position: absolute;
  left: 1350px;
  top: 200px;
  z-index: 1000;
}
.block3 {
  height: 800px;
  width: 500px;
  position: absolute;
  left: 1350px;
  top: 540px;
  z-index: 1000;
}
.el-carousel__item {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.carousel-image {
  max-width: 100%;
  max-height: 100%;
}

.webicon {
  font-family: 'Trebuchet';
  font-size: 50px;
  position: absolute;
  left: 380px;
  top: 100px;
}

.intro {
  width: 800px;
  position: absolute;
  left: 50px;
  top: 200px;
  z-index: 10;
}
.intro2{
  width: 800px;
  position: absolute;
  left: 50px;
  top: 200px;
  z-index: 200;
}

.el-collapse-item__header, el-collapse-item__header is-active {
  font-size: 20px !important;
}
.theme {
  position: absolute;
  left: 10px;
  top: 140px;
}
.background {
  position: absolute;
  left: 10px;
  right: 100px;
  width: 700px;
  height: 900px;
  z-index: 100;
}
.background2 {
  position: absolute;
  left: 310px;
  right: 100px;
  width: 700px;
  height: 900px;
  z-index: 100;
}
.background3 {
  position: absolute;
  left: 610px;
  right: 100px;
  width: 700px;
  height: 900px;
  z-index: 100;
}
.background4 {
  position: absolute;
  left: 910px;
  right: 100px;
  width: 700px;
  height: 900px;
  z-index: 100;
}
.background5 {
  position: absolute;
  left: 1210px;
  right: 100px;
  width: 700px;
  height: 900px;
  z-index: 100;
}
.background6 {
  position: absolute;
  left: 1510px;
  right: 100px;
  width: 700px;
  height: 900px;
  z-index: 100;
}
</style>
