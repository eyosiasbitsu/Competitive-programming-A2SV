function pivotArray(nums: number[], pivot: number): number[] {
    const less:number[] = []
    const greater: number[] = []
    const equal:number[] = []
    
    for(let item of nums){
        if(item > pivot){
            greater.push(item)
        }else if(item < pivot){
            less.push(item)
        }
        else{
            equal.push(item)
        }
    }
    return less.concat(equal).concat(greater)
};