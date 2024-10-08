const Tour=require('./../models/tourModel')


exports.getAllTours = (req, res) => {
  console.log(req.requestTime);

  res.status(200).json({
    status: 'success',
    requestedAt: req.requestTime,
    // results: tours.length,
    // data: {
    //   tours
    // }
  });
};

exports.getTour = (req, res) => {
  console.log(req.params);
  const id = req.params.id * 1;
};



exports.createTour =async (req, res) => {
  try {
    const newTour=await Tour.create(req.body);
    res.status(201).json({
      status: 'success',
      data:{
        tour:newTour
      }
    });
     
  } catch (error) {
    res.status(400).json({
      status:'fail',
      message:"Invalid data sent!"
    })
  }
};
 
exports.updateTour = (req, res) => {
  res.status(200).json({
    status: 'success',
    data: {
      tour: '<Updated tour here...>'
    }
  });
};

exports.deleteTour = (req, res) => {
  res.status(204).json({
    status: 'success',
    data: null
  });
};
