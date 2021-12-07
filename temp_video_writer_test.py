
pathOut = './ims/2/gan.mp4'
fps = 60

rn = ColoredRenderer()

## Assign attributes to renderer
w, h = (640, 480)

rn.camera = ProjectPoints(v=m, rt=np.zeros(3), t=np.array([0, 0, 2.]), f=np.array([w,w])/2., c=np.array([w,h])/2., k=np.zeros(5))
rn.frustum = {'near': 1., 'far': 10., 'width': w, 'height': h}
rn.set(v=m, f=m.f, bgcolor=np.zeros(3))

## Construct point light source
rn.vc = LambertianPointLight(
    f=m.f,
    v=rn.v,
    num_verts=len(m),
    light_pos=np.array([-1000,-1000,-2000]),
    vc=np.ones_like(m)*.9,
    light_color=np.array([1., 1., 1.]))

#adding pose!!!
frame_array = []
for i in range(len(pose)): 
    img = cv2.imread(path)
    height, width, layers = img.shape
    size = (width,height)


    m.pose[:] = pose[i]
    m.betas[:] = np.random.rand(m.betas.size) * .03
    m.pose[0] = np.pi


    frame_array.append(rn.r)
    print(i, 'is done...')

out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()