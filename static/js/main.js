

const citysDataBox = document.getElementById('city-data-box')
const cityInput = document.getElementById('cities')

const stationDataBox = document.getElementById('station-data-box')
const stationInput = document.getElementById('stations')

const stationText = document.getElementById('station-text')

$.ajax({
    type:'GET',
    url:'/city-json/',
    success:function(response){
        console.log(response.data)
        const citydata = response.data
        citydata.map(item =>{
            const option = document.createElement('div')
            option.textContent = item.cityname
            option.setAttribute('class','item')
            option.setAttribute('data-value',item.cityname)
            citysDataBox.appendChild(option)
        })
    },
    error:function(error){
        console.log(error)
    }
    })

cityInput.addEventListener('change',e=>{
     console.log(e.target.value)
    const selectedCity = e.target.value

    stationDataBox.innerHTML=""
    stationText.textContent="Choose your station"
    stationText.classList.add("default")

    $.ajax({
        type:'GET',
        url:`station-json/${selectedCity}/`,
        success:function(response){
            console.log(response.data)
            const stationData = response.data
            stationData.map(item=>{
                const option = document.createElement('div')
                option.textContent = item.stations
                option.setAttribute('class','item')
                option.setAttribute('data-value',item.stations)
                stationDataBox.appendChild(option)
            })
            },
            error:function(error){
            console.log(error)
            }
        })

})
